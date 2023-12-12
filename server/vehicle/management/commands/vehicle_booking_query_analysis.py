from datetime import datetime

from django.core.management.base import BaseCommand
from django.db.models import Q

from vehicle.models import PaymentStatus, Vehicle


class Command(BaseCommand):
    help = "Adds default users"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        start_date = datetime(2021, 7, 15)
        end_date = datetime(2021, 7, 25)
        exclude_bookings = Q(
            vehicle_bookings__pickup_date__lte=start_date,
            vehicle_bookings__next_available_date__gt=start_date,
            vehicle_bookings__payment_status=PaymentStatus.COMPLETE,
        )
        exclude_bookings |= Q(
            vehicle_bookings__pickup_date__lte=end_date,
            vehicle_bookings__next_available_date__gt=end_date,
            vehicle_bookings__payment_status=PaymentStatus.COMPLETE,
        )
        query = Vehicle.objects.exclude(exclude_bookings)
        print("*" * 10)
        print("This query ensures you dont get vehicles that are over lapping")
        print(query.query.__str__())
        print("*" * 10)

        print("*" * 10)
        print("Explain plan for this expensive query with index")
        print(query.explain())
        print("*" * 10)
