from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import User
from .serializer import UserSerializer


class SignUpView(APIView):

    permission_classes = [AllowAny] # noqa

    def post(self, request):
        # check if user exists in the system
        if User.objects.filter(email=request.data['email'], is_active=True).exists():
            return Response(data={'message': 'User already exits'}, status=status.HTTP_403_FORBIDDEN)

        # if user previously tried to create but did not verify email
        verified_user = UserSerializer(data={**request.data, 'is_active': False})
        if verified_user.is_valid():
            obj, _ = User.objects.get_or_create(email=request.data['email'], is_active=False)
            obj.set_password(request.data['password'])
            obj.save()
            resp = self.send_verification_email(request, obj)
            print(resp)
            return Response(
                {'message': 'User created, Please check your email to verify account'},
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
            return Response({'detail': 'Email successfully verified.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid verification link.'}, status=status.HTTP_400_BAD_REQUEST)
