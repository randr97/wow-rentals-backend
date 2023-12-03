from rest_framework import serializers

from .models import (
    OfficeLocation,
    VehicleClass,
    Vehicle,
    Booking,
)


class OfficeLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeLocation
        fields = '__all__'


class VehicleClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleClass
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


class BookingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
