from rest_framework import serializers

from .models import (Corporation, CouponCorporate, CouponIndividual,
                     CustomerCorporate, CustomerIndividual, Payment)


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, data):
        return {
            "payment_id": data.payment_id,
            "payment_method": data.payment_method,
            "card_number": data.card_number,
            "is_valid": data.is_valid,
        }


class CorporationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Corporation
        fields = '__all__'

    def to_representation(self, data):
        return {
            "name": data.name,
            "registration_number": data.registration_number,
            "domain": data.domain,
        }


class CustomerCorporateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerCorporate
        fields = '__all__'

    def to_representation(self, data):
        return {
            "payment": PaymentSerializer(Payment.objects.filter(customer_id=data.customer_id), many=True).data,
            "corporation": CorporationSerializer(data.corp_id).data,
            "emp_id": data.emp_id,
        }


class CustomerIndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerIndividual
        fields = '__all__'

    def to_representation(self, data):
        return {
            "payment": PaymentSerializer(Payment.objects.filter(customer_id=data.customer_id), many=True).data,
            "dl_number": data.dl_number,
            "insurance_company": data.insurance_company,
            "insurance_policy_no": data.insurance_policy_no,
        }


class CouponIndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = CouponIndividual
        fields = '__all__'


class CouponCorporateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CouponCorporate
        fields = '__all__'
