import logging
from datetime import datetime, timedelta

from django.conf import settings
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from .models import Booking, PaymentStatus

logger = logging.getLogger()


@db_periodic_task(crontab(minute='*/1'))
def clear_stray_bookings():
    bookings = Booking.objects.filter(
        created_at__lt=(datetime.now() - timedelta(seconds=settings.PAYMENT_SESSION_TIME)),
        payment_status=PaymentStatus.PENDING,
    )
    print("*" * 10)
    print("Deleting these bookings")
    print(list(bookings))
    print("*" * 10)
    bookings.delete()
