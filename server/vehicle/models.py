from datetime import timedelta

from django.conf import settings
# from django.contrib.gis.db import models as geo
from django.db import models
from django.utils.translation import gettext_lazy as _

from users_management.models import User


class TripStatus(models.TextChoices):
    PENDING = "P", _("PENDING")
    ONGOING = "O", _("ONGOING")
    ABORTED = "A", _("ABORTED")
    COMPLETE = "C", _("COMPLETE")


class OfficeLocation(models.Model):
    location_id = models.BigAutoField(primary_key=True)

    address_street = models.CharField(max_length=100, null=False, blank=False)
    address_city = models.CharField(max_length=100, null=False, blank=False)
    address_state = models.CharField(max_length=100, null=False, blank=False, choices=settings.STATE_CHOICES)
    address_zipcode = models.CharField(max_length=100, null=False, blank=False)

    # lat = geo.PointField(null=False, blank=False)
    # lan = geo.PointField(null=False, blank=False)

    phone = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        indexes = [
            # models.Index(fields=['lat']),
            # models.Index(fields=['lan']),
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
    class_id = models.OneToOneField(VehicleClass, on_delete=models.SET_NULL, null=True)
    make = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    vin_number = models.CharField(max_length=100, null=False, blank=False)
    license_plate_number = models.CharField(max_length=100, null=False, blank=False)
    make_year = models.DateField(null=False, blank=False)

    odo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.make}-{self.model}"


class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    customer_id = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name='user_bookings')
    vehicle_id = models.OneToOneField(
        Vehicle, on_delete=models.SET_NULL, null=True, related_name='vehicle_bookings')

    pickup_date = models.DateField(null=False, blank=False)
    pickup_location = models.OneToOneField(
        OfficeLocation, on_delete=models.SET_NULL, null=True, related_name='pickup_bookings')

    dropoff_date = models.DateField(null=False, blank=False)
    dropoff_location = models.OneToOneField(
        OfficeLocation, on_delete=models.SET_NULL, null=True, related_name='dropoff_bookings')

    start_odo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    end_odo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)

    daily_limit = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    trip_status = models.CharField(max_length=1, null=False, blank=False, choices=TripStatus.choices)

    next_available_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.booking_id

    def save(self, *args, **kwargs):
        self.next_available_date = self.dropoff_date + timedelta(days=1)
        if self.pickup_location != self.dropoff_location:
            self.next_available_date = self.dropoff_date + timedelta(days=1)
        super().save(*args, **kwargs)
