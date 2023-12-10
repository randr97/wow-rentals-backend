from django.contrib.auth.views import (PasswordChangeDoneView,
                                       PasswordResetConfirmView)
from django.urls import path
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenObtainPairView,
                                            TokenRefreshView)

from .views import ForgotPasswordView, ProfileView, SignUpView, VerifyEmailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/<str:uidb64>/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('profile/', ProfileView.as_view({'get': 'get_profile', 'post': 'update_profile'}), name='get-edit-profile'),
    path('password/', ProfileView.as_view({'post': 'update_password'}), name='update-password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/done/', PasswordChangeDoneView.as_view(), name='password_reset_complete'),
] + [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
