from django.urls import path
from .views import SignUpView, VerifyEmailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/<str:uidb64>/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
]
