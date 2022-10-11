from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField, ReadOnlyField


from .models import *




class ContractSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.name')

    class Meta:
        fields = ('id', 'name', 'phone','nationalId', 'area', 'streetName', 'addressBuilding','addressApartment','addressDetails','created_at_date')
    # client = ClientSerializer(read_only=True)

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
        fields = '__all__'
