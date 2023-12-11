import random
from decimal import Decimal
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker

from users_management.models import User
from vehicle.models import Booking, OfficeLocation, Vehicle
from swimlane.models import Coupon, CouponCorporate, CouponIndividual, Payment


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        fake = Faker()
        vehicles = [v.pk for v in Vehicle.objects.all()]
        offices = [o.pk for o in OfficeLocation.objects.all()]
        users = []
        for u in User.objects.all():
            if Payment.objects.filter(customer_id=u.customer_id).exists():
                users.append(u.pk)
        corp_coupon = [c.pk for c in CouponCorporate.objects.all()]
        inv_coupon = [c.pk for c in CouponIndividual.objects.all()]

        for i in range(10 ** 5):
            v = Vehicle.objects.get(pk=random.choice(vehicles))
            b = Booking(
                pk=i + 100000,
                pickup_date=fake.date_between_dates(date_start=datetime(2018, 1, 1), date_end=datetime(2023, 10, 1)),
                pickup_location=v.location_id,
                dropoff_location=OfficeLocation.objects.get(pk=random.choice([v.location_id.pk] * 10 + offices)),
                start_odo=v.odo,
                end_odo=v.odo + Decimal(random.uniform(100, 1000)),
                daily_limit=100,
                trip_status='O',
                customer_id=User.objects.get(pk=random.choice(users)),
                vehicle_id=v,
                coupon_id=None,
            )
            if b.customer_id.user_type == 'C':
                b.coupon_id = Coupon.objects.get(pk=random.choice(corp_coupon))
            else:
                b.coupon_id = Coupon.objects.get(pk=random.choice(inv_coupon))
            b.dropoff_date = b.pickup_date + timedelta(days=int(random.uniform(1, 9)))
            b.save()
            b.payment.set(Payment.objects.filter(customer_id=b.customer_id.pk))
            b.trip_status = 'C'
            b.save()

        self.stdout.write(
            self.style.SUCCESS('Booking bulk created')
        )
