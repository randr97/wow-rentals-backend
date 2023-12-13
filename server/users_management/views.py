from django.conf import settings
from django.contrib.auth.tokens import (PasswordResetTokenGenerator,
                                        default_token_generator)
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from swimlane.models import Corporation

from .models import User, UserType
from .serializer import UserSerializer


class SignUpView(APIView):

    permission_classes = [AllowAny] # noqa

    def post(self, request):
        # check if user exists in the system
        if User.objects.filter(email=request.data['email'], is_active=True).exists():
            return Response(data={'message': 'User already exits'}, status=status.HTTP_403_FORBIDDEN)

        user_type = UserType.CORPORATE if Corporation.objects.filter(
            domain=request.data['email'].split('@')[1]
        ).exists() else UserType.INDIVIDUAL

        # if user previously tried to create but did not verify email delete it
        User.objects.filter(email=request.data['email'], is_active=False).delete()
        verified_user = UserSerializer(data={**request.data, 'is_active': False, 'user_type': user_type})
        if verified_user.is_valid(raise_exception=True):
            verified_user = verified_user.save()
            self.send_verification_email(request, verified_user)
            return Response(
                {'message': 'User created! Please check your email to verify account!'},
                status=status.HTTP_201_CREATED
            )
        return Response({'message': 'Invalid user data'}, status=status.HTTP_400_BAD_REQUEST)

    def send_verification_email(self, request, user):
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        verification_link = f"{settings.HOST_URL}/user/verify/{uidb64}/{token}"
        subject = '[Wow Rentals] Verify Your Email'
        message = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email Verification</title>
        </head>
        <body>
            <div style="text-align: center; padding: 20px;">
                <h2>Email Verification</h2>
                <p>Thank you for signing up! Click the button below to verify your email:</p>
                <a href="{verification_link}" style="display: inline-block; padding: 10px 20px; background-color: #007BFF; color: #ffffff; text-decoration: none; border-radius: 5px;">
                    Verify Email
                </a>
            </div>
        </body>
        </html>
        """
        return send_mail(subject, 'Click to verify link', settings.EMAIL_HOST_USER, [user.email], html_message=message)


class VerifyEmailView(APIView):

    permission_classes = [AllowAny] # noqa

    def post(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'message': 'Email not found!'}, status=status.HTTP_404_NOT_FOUND)

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            if "password" in request.data:
                user.set_password(request.data["password"])
            user.save()
        return Response({'message': 'Email verified!'}, status=status.HTTP_200_OK)


class ForgotPasswordView(APIView):

    permission_classes = [AllowAny] # noqa

    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if user:
            self.send_reset_email(request, user)
            return Response({'message': 'Password reset email sent successfully!'}, status=status.HTTP_200_OK)
        return Response({'message': 'Email does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    def send_reset_email(self, request, user):
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        reset_link = f"{settings.HOST_URL}/user/new-password/{uidb64}/{token}/"
        subject = '[Wow Rentals] Password Reset'
        message = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email Verification</title>
        </head>
        <body>
            <div style="text-align: center; padding: 20px;">
                <h2>Email Verification</h2>
                <p>Click link to reset your password:</p>
                <a href="{reset_link}" style="display: inline-block; padding: 10px 20px; background-color: #007BFF; color: #ffffff; text-decoration: none; border-radius: 5px;">
                    Verify Email
                </a>
            </div>
        </body>
        </html>
        """
        return send_mail(subject, 'Click to verify link', settings.EMAIL_HOST_USER, [user.email], html_message=message)


class ProfileView(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def get_profile(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def update_profile(self, request):
        sez = UserSerializer(instance=request.user, data=request.data)
        if sez.is_valid(raise_exception=True):
            sez.save()
            return Response(data=sez.data, status=status.HTTP_200_OK)
        return Response({'message': sez.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update_password(self, request):
        user = request.user
        if user.check_password(request.data["old_password"]):
            user.set_password(request.data["new_password"])
            user.save()
            return Response({'message': 'Password reset success'}, status=status.HTTP_200_OK)
        return Response(
            {
                'message': 'Wrong Password! Please check old password and try again!'
            }, status=status.HTTP_400_BAD_REQUEST
        )
