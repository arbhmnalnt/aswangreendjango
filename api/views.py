from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from DataEntry.models import *
from django.core import serializers as core_serializers
from DataEntry.serializers import ContractSerializer, ServiceSerializer, ClientSerializer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# create
## APIView create operation
class addClient(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
## APIView view all operation or a specific record
class getClients(APIView):
    def get(self,request, *args, **kwargs):
        try:
            serialNum = request.query_params["serialNumber"]
            if serialNum != None:
                client=Client.objects.get(serialNum==serialNum)
                data = ClientSerializer(client, many=False).data
        except:



        clients=Client.objects.all()
        data = ClientSerializer(clients, many=True).data
        return Response(data)
## APIView view record operation
class getClientBySerialNum(APIView):
    def get(self,request,serialNum):
        try:
            client=Client.objects.get(serialNum==serialNum)
            data = ClientSerializer(client, many=False).data
        except ObjectDoesNotExist:
            data = {'erorr':'no client found by this serial number'}
        return Response(data)


# get data from request vars
# def get(self,request,*args,**kwargs): #or def list()
#     data = request.GET.get('name')

# ## APIView update operation
# class getClients(APIView):
#     def get_client(identifier):

#         return
#     def get(self,request,identifier):
#         clients=get_client(identifier)
#         data = ContractSerializer(clients, many=True).data
#         return Response(data)