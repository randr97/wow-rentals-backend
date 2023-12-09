from datetime import datetime

from rest_framework import serializers

from .models import (Corporation, Coupon, CouponChoice, CouponCorporate,
                     CouponIndividual, CustomerCorporate, CustomerIndividual,
                     Payment)


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
            "card_name": data.card_name,
            "card_exp_date": datetime.strftime(data.card_exp_date, '%Y-%m'),
            "card_zipcode": data.card_zipcode,
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


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'

    def to_representation(self, data):
        res = {
            "coupon_id": data.coupon_id,
            "coupon_code": data.coupon_code,
            "coupon_type": data.coupon_type,
            "discount": data.discount,
            "is_valid": data.is_valid,
        }
        try:
            if data.coupon_type == CouponChoice.CORPORATE:
                res.update({
                    "corporate_coupon": CouponCorporateSerializer(data.corporate_coupon).data
                })
            else:
                res.update({
                    "individual_coupon": CouponIndividualSerializer(data.individual_coupon).data
                })
        except Exception as e:
            print(f"Coupon Incomplete: {e}")
            res = {}
        return res


class CouponIndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = CouponIndividual
        fields = '__all__'


class CouponCorporateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CouponCorporate
        fields = '__all__'
