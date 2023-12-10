import random
from datetime import datetime
from decimal import Decimal

import pytz  # noqa
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users_management.models import UserType
from users_management.serializer import UserSerializer
from vehicle.models import (Booking, OfficeLocation, PaymentStatus, TripStatus,
                            Vehicle)
from vehicle.serializer import BookingsSerializer

from .models import (Corporation, Coupon, CouponCorporate, CouponIndividual,
                     CustomerCorporate, CustomerIndividual, Payment)
from .serializer import (CouponSerializer, CustomerCorporateSerializer,
                         CustomerIndividualSerializer, PaymentSerializer)


class HomeView(viewsets.ViewSet):

    permission_classes = [IsAuthenticated] # noqa

    def metadata(self, request):
        CustomerModel, CustomerSerializer = {
            UserType.INDIVIDUAL: (CustomerIndividual, CustomerIndividualSerializer),
            UserType.CORPORATE: (CustomerCorporate, CustomerCorporateSerializer),
        }[request.user.user_type]
        cus_data = CustomerSerializer(CustomerModel.objects.filter(customer_id=request.user), many=True).data
        resp = {
            "is_profile_complete": True if cus_data else False,
            "individual_customer": CustomerIndividualSerializer(CustomerIndividual.objects.filter(customer_id=request.user), many=True).data,
            "corporate_customer": CustomerCorporateSerializer(CustomerCorporate.objects.filter(customer_id=request.user), many=True).data,
            "user": UserSerializer(request.user).data,
            "payment": PaymentSerializer(Payment.objects.filter(customer_id=request.user.pk), many=True).data,
        }
        return Response(data=resp, status=status.HTTP_200_OK)

    def update_customer(self, request):
        CustomerModel, CustomerSerializer = {
            UserType.INDIVIDUAL: (CustomerIndividual, CustomerIndividualSerializer),
            UserType.CORPORATE: (CustomerCorporate, CustomerCorporateSerializer),
        }[request.user.user_type]
        request.data['customer_id'] = request.user.pk
        if request.user.user_type == UserType.CORPORATE:
            request.data['corp_id'] = Corporation.objects.filter(
                domain=request.user.email.split('@')[1]).first().pk
        if CustomerModel.objects.filter(customer_id=request.user).exists():
            sez = CustomerSerializer(instance=CustomerModel.objects.get(customer_id=request.user), data=request.data)
            if sez.is_valid(raise_exception=True):
                sez.save()
                return Response(sez.data, status=status.HTTP_200_OK)
        sez = CustomerSerializer(data=request.data)
        if sez.is_valid(raise_exception=True):
            sez.save()
        return Response(sez.data, status=status.HTTP_200_OK)

    def get_customer(self, request):
        try:
            if request.user.user_type == UserType.INDIVIDUAL:
                customer, CustomerSerializer = (request.user.individual_customer, CustomerIndividualSerializer)
            else:
                customer, CustomerSerializer = (request.user.corporate_customer, CustomerCorporateSerializer)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': 'Customer details unavailable'}, status=status.HTTP_404_NOT_FOUND)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "payment": PaymentSerializer(
                    Payment.objects.filter(customer_id=request.user, is_valid=True), many=True).data
            }
        )

    def post(self, request):
        request.data["customer_id"] = request.user.pk
        request.data["card_exp_date"] = datetime.strptime(request.data["card_exp_date"], '%Y-%m').date()
        sez = PaymentSerializer(data=request.data)
        if sez.is_valid(raise_exception=True):
            sez.save()
        return Response(sez.data, status=status.HTTP_200_OK)

    def delete(self, request):
        pay = Payment.objects.get(customer_id=request.user, payment_id=request.GET["payment_id"])
        pay.is_valid = False
        pay.save()
        return Response({'message': 'Payment method deleted'}, status=status.HTTP_200_OK)


class CouponView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.user_type == UserType.INDIVIDUAL:
            query = Q(individual_coupon__valid_to__gte=datetime.now().date())
        else:
            query = Q(corporate_coupon__corp_id=request.user.corporate_customer.corp_id)
        query &= Q(coupon_type=request.user.user_type, is_valid=True)
        return Response(
            CouponSerializer(
                Coupon.objects.filter(query).order_by('pk'), many=True, allow_null=False).data,
            status=status.HTTP_200_OK
        )


def coupon_is_valid(request):
    try:
        is_valid = (
            request.user.user_type == UserType.INDIVIDUAL and
            CouponIndividual.objects.filter(
                coupon_id=Coupon.objects.filter(coupon_code=request.data["coupon_code"]).first(),
                valid_to__gte=datetime.now().date()
            ).count()
        ) or (
            request.user.user_type == UserType.CORPORATE and
            CouponCorporate.objects.filter(
                coupon_id=Coupon.objects.filter(coupon_code=request.data["coupon_code"]).first(),
                corp_id=request.user.corporate_customer.corp_id
            ).count()
        )
    except Exception as e:
        print(e)
        is_valid = False
    return is_valid


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_coupon(request):
    return Response({'is_valid': coupon_is_valid(request)}, status=status.HTTP_201_CREATED)


class BookView(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def pending_booking(self, request):
        try:
            booking = Booking(
                vehicle_id=Vehicle.objects.get(pk=request.data["vehicle_id"]),
                customer_id=request.user,
                pickup_date=datetime.strptime(request.data["pickup_date"], "%Y-%m-%d"),
                pickup_location=OfficeLocation.objects.get(pk=request.data["pickup_location"]),
                dropoff_date=datetime.strptime(request.data["dropoff_date"], "%Y-%m-%d"),
                dropoff_location=OfficeLocation.objects.get(pk=request.data["dropoff_location"]),
            ).book_vehicle()
            return Response(BookingsSerializer(booking).data, status=status.HTTP_200_OK)
        except ValueError as e:
            print(e)
            return Response({'message': 'Bad Request!'}, status=status.HTTP_400_BAD_REQUEST)

    def complete_booking(self, request):
        booking = Booking.objects.get(
            pk=request.data["booking_id"],
            customer_id=request.user,
            trip_status=TripStatus.PENDING,
            payment_status=PaymentStatus.PENDING,
        )
        if (timezone.now() - booking.created_at).total_seconds() >= settings.PAYMENT_SESSION_TIME:
            return Response({'message': 'Booking session cancelled'}, status=status.HTTP_403_FORBIDDEN)
        if "coupon_code" in request.data and coupon_is_valid(request):
            booking.coupon_id = Coupon.objects.get(coupon_code=request.data["coupon_code"]).pk
        if Payment.objects.filter(customer_id=request.user, pk__in=request.data["payment_id"]).exists():
            booking.payment_status = PaymentStatus.COMPLETE
            booking.payment.set(
                Payment.objects.filter(
                    customer_id=request.user,
                    pk__in=request.data["payment_id"]
                )
            )
            booking.save()
            return Response({'message': 'Payment Successful!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Request!'}, status=status.HTTP_400_BAD_REQUEST)

    def update_booking(self, request):
        booking = Booking.objects.get(
            pk=request.data["booking_id"],
            customer_id=request.user,
            trip_status__in=[TripStatus.PENDING, TripStatus.ONGOING],
            payment_status=PaymentStatus.COMPLETE,
        )
        if request.data.get("dropoff_location"):
            booking.dropoff_location = OfficeLocation.objects.get(pk=request.data.get("dropoff_location"))
        if "payment_id" in request.data and Payment.objects.filter(
                customer_id=request.user,
                pk__in=request.data["payment_id"]).exists():

            booking.payment.set(
                Payment.objects.filter(customer_id=request.user, pk__in=request.data["payment_id"])
            )
        booking.save()
        booking.refresh_from_db()
        return Response(BookingsSerializer(booking).data, status=status.HTTP_200_OK)

    def start_booking(self, request):
        booking = Booking.objects.get(
            pk=request.data["booking_id"],
            customer_id=request.user,
            trip_status__in=TripStatus.PENDING,
            payment_status=PaymentStatus.COMPLETE,
        )
        booking.trip_status = TripStatus.ONGOING
        booking.start_odo = random.uniform(20000, 80000)
        booking.save()
        return Response(BookingsSerializer(booking).data, status=status.HTTP_200_OK)

    def end_booking(self, request):
        booking = Booking.objects.get(
            pk=request.data["booking_id"],
            customer_id=request.user,
            trip_status__in=TripStatus.ONGOING,
            payment_status=PaymentStatus.COMPLETE,
        )
        booking.trip_status = TripStatus.COMPLETE
        booking.end_odo = booking.start_odo + Decimal(random.uniform(100, 1000))
        booking.save()
        return Response(BookingsSerializer(booking).data, status=status.HTTP_200_OK)

    def list_bookings(self, request):
        sez = BookingsSerializer(
            Booking.objects.filter(
                customer_id=request.user, payment_status=PaymentStatus.COMPLETE).order_by('pickup_date'),
            many=True,
        )
        return Response(sez.data, status=status.HTTP_200_OK)
