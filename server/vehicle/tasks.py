from datetime import datetime, timedelta
from django.conf import settings
from .models import Booking, PaymentStatus
from .serializer import BookingsSerializer
from background_task import background


@background(schedule=30)
def clear_stray_bookings():
    data = BookingsSerializer(
        Booking.objects.filter(
            created_at__lt=(datetime.now() - timedelta(seconds=settings.PAYMENT_SESSION_TIME)),
            payment_status=PaymentStatus.PENDING,
        )
    ).data
    print(data)
