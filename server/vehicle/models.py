from datetime import datetime, timedelta

from django.conf import settings
# from django.contrib.gis.db import models as geo
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from swimlane.models import Coupon, Payment
from users_management.models import User


class TripStatus(models.TextChoices):
    PENDING = "P", _("PENDING")
    ONGOING = "O", _("ONGOING")
    ABORTED = "A", _("ABORTED")
    COMPLETE = "C", _("COMPLETE")


class PaymentStatus(models.TextChoices):
    PENDING = "P", _("PENDING")
    COMPLETE = "C", _("COMPLETE")


class OfficeLocation(models.Model):
    location_id = models.BigAutoField(primary_key=True)

    address_street = models.CharField(max_length=100, null=False, blank=False)
    address_city = models.CharField(max_length=100, null=False, blank=False)
    address_state = models.CharField(max_length=100, null=False, blank=False, choices=settings.STATE_CHOICES)
    address_zipcode = models.CharField(max_length=100, null=False, blank=False)

    phone = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['address_city']),
            models.Index(fields=['address_street']),
        ]

    def __str__(self):
        return self.address_street


class VehicleClass(models.Model):
    class_id = models.BigAutoField(primary_key=True)
    vehicle_class = models.CharField(max_length=100, null=False, blank=False)
    rent_charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    extra_charge = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.vehicle_class


class Vehicle(models.Model):
    vehicle_id = models.BigAutoField(primary_key=True)
    location_id = models.ForeignKey(OfficeLocation, on_delete=models.CASCADE)
    class_id = models.ForeignKey(VehicleClass, on_delete=models.SET_NULL, null=True)
    make = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    vin_number = models.CharField(max_length=100, null=False, blank=False)
    license_plate_number = models.CharField(max_length=100, null=False, blank=False)
    make_year = models.DateField(null=False, blank=False)
    odo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    rating = models.IntegerField(default=4, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.make}-{self.model}"


class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    customer_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='user_bookings')
    vehicle_id = models.ForeignKey(
        Vehicle, on_delete=models.SET_NULL, null=True, related_name='vehicle_bookings')

    pickup_date = models.DateField(null=False, blank=False)
    pickup_location = models.ForeignKey(
        OfficeLocation, on_delete=models.SET_NULL, null=True, related_name='pickup_bookings')

    dropoff_date = models.DateField(null=False, blank=False)
    dropoff_location = models.ForeignKey(
        OfficeLocation, on_delete=models.SET_NULL, null=True, related_name='dropoff_bookings')

    start_odo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False, default=None)
    end_odo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False, default=None)

    daily_limit = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    trip_status = models.CharField(max_length=1, null=False, blank=False, choices=TripStatus.choices)

    next_available_date = models.DateField(null=True, blank=True)

    coupon_id = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, related_name='user_coupons')

    payment_status = models.CharField(max_length=1, choices=PaymentStatus.choices, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    payment = models.ManyToManyField(Payment, related_name='paid_bookings')

    class Meta:
        indexes = [
            models.Index(fields=['vehicle_id', 'pickup_date']),
            models.Index(fields=['vehicle_id', 'dropoff_date']),
            models.Index(fields=['vehicle_id', 'next_available_date']),
        ]

    def __str__(self):
        return str(self.booking_id)

    def save(self, *args, **kwargs):
        self.next_available_date = self.dropoff_date + timedelta(days=1)
        if self.pickup_location != self.dropoff_location:
            self.next_available_date = self.dropoff_date + timedelta(days=1)
        super().save(*args, **kwargs)

    def book_vehicle(self):
        with transaction.atomic():
            # Check for existing bookings for the given vehicle and overlapping dates
            query = models.Q(
                vehicle_id=self.vehicle_id,
                pickup_date__lte=self.pickup_date,
                next_available_date__gt=self.pickup_date,
                payment_status=PaymentStatus.COMPLETE,
            )
            query |= models.Q(
                vehicle_id=self.vehicle_id,
                pickup_date__lte=self.dropoff_date,
                next_available_date__gt=self.dropoff_date,
                payment_status=PaymentStatus.COMPLETE,
            )
            query |= models.Q(
                vehicle_id=self.vehicle_id,
                pickup_date__lte=self.pickup_date,
                next_available_date__gt=self.pickup_date,
                payment_status=PaymentStatus.PENDING,
                created_at__gt=(datetime.now() - timedelta(seconds=settings.PAYMENT_SESSION_TIME)),
            )
            query |= models.Q(
                vehicle_id=self.vehicle_id,
                pickup_date__lte=self.dropoff_date,
                next_available_date__gt=self.dropoff_date,
                payment_status=PaymentStatus.PENDING,
                created_at__gt=(datetime.now() - timedelta(seconds=settings.PAYMENT_SESSION_TIME)),
            )
            existing_bookings = Booking.objects.filter(query).exclude(
                booking_id=self.booking_id
            )

            if existing_bookings.exists():
                raise ValueError("Vehicle is already booked for the selected dates.")

            # Create a new booking with 'pending_payment' status
            new_booking = Booking(
                customer_id=self.customer_id,
                vehicle_id=self.vehicle_id,
                pickup_date=self.pickup_date,
                dropoff_date=self.dropoff_date,
                pickup_location=self.pickup_location,
                dropoff_location=self.dropoff_location,
                payment_status=PaymentStatus.PENDING,
                trip_status=TripStatus.PENDING,
                daily_limit=100,
            )
            new_booking.save()
            new_booking.refresh_from_db()
            return new_booking
