from rest_framework import serializers

from swimlane.serializer import CouponSerializer, PaymentSerializer

from .models import Booking, OfficeLocation, Vehicle, VehicleClass


class OfficeLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeLocation
        fields = '__all__'


class VehicleClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleClass
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):

    class_id = VehicleClassSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'


class BookingsSerializer(serializers.ModelSerializer):
    vehicle_id = VehicleSerializer()
    pickup_location = OfficeLocationSerializer()
    dropoff_location = OfficeLocationSerializer()
    coupon_id = CouponSerializer()
    payment = PaymentSerializer(many=True)

    class Meta:
        model = Booking
        fields = '__all__'
