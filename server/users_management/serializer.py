from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    password = serializers.CharField(write_only=True, required=False)
    user_type = serializers.CharField(write_only=True, required=False)

    def create(self, data):
        obj = User(**data)
        obj.set_password(data['password'])
        obj.save()
        return obj

    def update(self, instance, data):
        for i in ['email', 'password', 'user_type']:
            if i in data:
                data.pop(i)
        instance.phone = data.get('phone', instance.phone)
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.address_street = data.get('address_street', instance.address_street)
        instance.address_city = data.get('address_city', instance.address_city)
        instance.address_state = data.get('address_state', instance.address_state)
        instance.address_zipcode = data.get('address_zipcode', instance.address_zipcode)
        instance.save()
        return instance

    def to_representation(self, data):
        return {
            "email": data.email,
            "phone": data.phone,
            "first_name": data.first_name,
            "last_name": data.last_name,
            "address_street": data.address_street,
            "address_city": data.address_city,
            "address_state": data.address_state,
            "address_zipcode": data.address_zipcode,
            "user_type": data.user_type,
        }
