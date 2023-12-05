import random
from datetime import datetime, timedelta
from faker import Faker

from django.core.management.base import BaseCommand

from users_management.models import User
from vehicle.models import Vehicle, Booking, OfficeLocation, VehicleClass


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        pass

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(10 ** 4):
            Vehicle(
                pk=i + 1000,
                location_id=OfficeLocation.objects.get(pk=1),
                class_id=VehicleClass.objects.get(pk=1),
                make='_'.join(fake.name().lower().split(' ')),
                model='_'.join(fake.name().lower().split(' ')),
                make_year='2022-01-01',
                vin_number='VIN' + "_".join(fake.name().lower().split(' ')),
                license_plate_number='LIC' + "_".join(fake.name().lower().split(' ')),
                odo=random.uniform(27000, 100000)
            ).save()

        bookings = []
        for i in range(10 ** 5):
            if i % 10000 == 0:
                Booking.objects.bulk_create(bookings)
                bookings = []
                print(f'Booking number {i} created')
            v = Vehicle.objects.get(pk=int(random.uniform(1000, 10000)))
            b = Booking(
                pk=i + 1000,
                pickup_date=fake.date_between_dates(date_start=datetime(2018, 1, 1), date_end=datetime(2024, 1, 1)),
                pickup_location=v.location_id,
                dropoff_location=v.location_id,
                start_odo=random.uniform(10000, 30000),
                end_odo=random.uniform(30000, 40000),
                daily_limit=65.00,
                trip_status='C',
                customer_id=User.objects.get(pk=6),
                vehicle_id=v,
                coupon_id=None,
            )
            b.dropoff_date = b.pickup_date + timedelta(days=int(random.uniform(1, 9)))
            bookings.append(b)

        self.stdout.write(
            self.style.SUCCESS('Booking bulk created')
        )
