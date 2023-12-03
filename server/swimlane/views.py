from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users_management.models import UserType

from .models import (Corporation, Coupon, CustomerCorporate,
                     CustomerIndividual, Payment)
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
            "customer_data": cus_data,
            "user_type": request.user.user_type,
        }
        return Response(data=resp, status=status.HTTP_200_OK)

    def customer(self, request):
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


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "payment": PaymentSerializer(
                    Payment.objects.filter(customer_id=request.user), many=True).data
            }
        )

    def post(self, request):
        request.data["customer_id"] = request.user.pk
        sez = PaymentSerializer(data=request.data)
        if sez.is_valid():
            sez.save()
            return Response(sez.data, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid information'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Payment.objects.filter(customer_id=request.user, payment_id=request.data["payment_id"]).delete()
        return Response({'message': 'Payment method deleted'}, status=status.HTTP_200_OK)


class CouponView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            CouponSerializer(
                Coupon.objects.filter(
                    coupon_type=request.user.user_type,
                    is_valid=True
                ).order_by('pk'), many=True, allow_null=False).data,
            status=status.HTTP_200_OK
        )
