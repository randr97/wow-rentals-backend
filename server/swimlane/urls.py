from django.urls import path

from .views import HomeView, PaymentView, CouponView

urlpatterns = [
    path('metadata/', HomeView.as_view({'get': 'metadata'}), name='home-apis-meta'),
    # to test
    path('customer/', HomeView.as_view({'post': 'customer'}), name='home-apis-customer-create-update'),
    path('payment/', PaymentView.as_view(), name='payment-apis-customer-create-update-get'),
    path('coupon/', CouponView.as_view(), name='coupon-apis-get'),
]
