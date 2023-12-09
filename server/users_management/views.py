from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
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
        base_url = f"{request.scheme}://{get_current_site(request)}"
        verification_link = f"{base_url}/user/verify/{uidb64}/{token}"
        subject = '[Wow Rentals] Verify Your Email'
        message = f'Click the following link to verify your email: {verification_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])


class VerifyEmailView(APIView):

    permission_classes = [AllowAny] # noqa

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
        return redirect('/')


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
