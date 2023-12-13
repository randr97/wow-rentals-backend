from django.urls import path

from .views import BookView, CouponView, HomeView, PaymentView

urlpatterns = [
    path('metadata/', HomeView.as_view({'get': 'metadata'}), name='home-apis-meta'),

    path('customer/', HomeView.as_view({'post': 'update_customer', 'get': 'get_customer'}), name='home-apis-customer-get-create-update'),
    path('payment/', PaymentView.as_view(), name='payment-apis-customer-create-update-get'),
    path('coupon/', CouponView.as_view(), name='coupon-apis-get'),
    path('coupon/validate/', BookView.as_view({'post': 'validate_coupon'}), name='validate-coupon'),
    # bookings apis
    path('booking/begin/', BookView.as_view({'post': 'pending_booking'}), name='booking-begin'),
    path('booking/complete/', BookView.as_view({'post': 'complete_booking'}), name='booking-complete'),
    path('booking/update/', BookView.as_view({'post': 'update_booking'}), name='booking-update'),
    path('booking/start/', BookView.as_view({'post': 'start_booking'}), name='booking-start'),
    path('booking/end/', BookView.as_view({'post': 'end_booking'}), name='booking-end'),
    path('booking/', BookView.as_view({'get': 'list_bookings'}), name='booking-list'),
]
