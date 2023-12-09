from datetime import datetime, timedelta

from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OfficeLocation, Vehicle
from .serializer import OfficeLocationSerializer, VehicleSerializer


class VehicleAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        start_date = datetime.strptime(request.data['pickup_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.data['dropoff_date'], '%Y-%m-%d')
        if end_date - start_date > timedelta(days=30):
            return Response({'message': 'Max booking days is 30!'}, status=status.HTTP_400_BAD_REQUEST)
        query = (
            ~Q(
                vehicle_bookings__pickup_date__range=[start_date, end_date],
                vehicle_bookings__dropoff_date__range=[start_date, end_date],
            )
        ) & Q(location_id__address_city=request.data["pickup_location"])
        if request.data.get('make'):
            query &= Q(make__in=request.data.get('make'))
        if request.data.get('model'):
            query &= Q(model__in=request.data.get('model'))
        if request.data.get('class_id'):
            query &= Q(class_id__in=request.data.get('class_id'))
        if request.data.get('vehicle_id__gt'):
            query &= Q(vehicle_id__gt=request.data.get('vehicle_id__gt'))
        data = VehicleSerializer(Vehicle.objects.filter(query).order_by('vehicle_id')[:1000], many=True).data
        return Response({
            "data": data,
            "has_next": False if len(data) < 1000 else True,
        }, status=status.HTTP_200_OK)


class LocationAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            return Response(
                OfficeLocationSerializer(
                    OfficeLocation.objects.filter(address_city__icontains=request.GET['address_city'])[: 10],
                    many=True
                ).data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
