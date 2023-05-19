from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField, ReadOnlyField


from .models import *




class ContractSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.name')

    class Meta:
        model = Contract
        fields = '__all__'


# class AreaeSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        # fields = ('name', 'created_at_date', 'price',)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone','password','nationalId', 'area', 'streetName', 'addressBuilding','addressApartment','addressDetails','created_at_date')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        # fields = '__all__'
