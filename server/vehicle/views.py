from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OfficeLocation
from .serializer import OfficeLocationSerializer


class VehicleAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        pass


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
