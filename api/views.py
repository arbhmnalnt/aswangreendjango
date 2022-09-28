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

def testing2(request):
    return HttpResponse("testing")

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
        def get(self, request):
            clients=Client.objects.all()
            data = ClientSerializer(clients, many=True).data
            return Response(data)
## APIView view record operation
class getClientBySerialNum(APIView):
    def get(self,request,serialNum):
        try:
            client=Client.objects.get(serialNum=serialNum)
            data = ClientSerializer(client, many=False).data
        except ObjectDoesNotExist:
            data = {'erorr':'no client found by this serial number'}
        return Response(data)

## aPIView view specific recor by value or view many recors based on the key
class getClientByKey(APIView):
    def get(self,request):
        try:
            client_id   = request.GET.get('id' , '0')
            serialNum   = request.GET.get('serialNum' , '0')
            phoneNumber = request.GET.get('phone' , '0')
            name        = request.GET.get('name' , '0')
            if serialNum != '0':
                client=Client.objects.get(serialNum=serialNum)
                data = ClientSerializer(client, many=False).data
            elif phoneNumber != '0':
                client=Client.objects.get(phoneNumber=phone)
                data = ClientSerializer(client, many=False).data
            elif name != '0':
                clients = Client.objects.filter(name__contains=str(name))
                data = ClientSerializer(clients, many=True).data
            elif client_id != '0':
                client = Client.objects.get(pk=client_id)
                data = ClientSerializer(client).data
            else:
                data = {'erorr', 'no key provided'}

        except Exception  as e:
            data = {'erorr':'erorr occured here'}
        return Response(data)

class collection_stats(APIView):
    def get(self, request):
        curr_count = Client.objects.filter(is_deleted=False).count()
        follows =  FollowContractServices.objects.filter(collcetStatusNums=2,is_deleted=False)
        req_counter = 0
        req_clients_list = []
        for follow in follows:
            if follow.client not in req_clients_list:
                req_counter +=1
                client=follow.client
                req_clients_list.append(client)
            else:
                continue
        req_count  = req_counter
        coll_count  = curr_count-req_count
        data = {'currentClients': curr_count, 'remainingCollections': req_count, 'collected': coll_count}
        return Response(data)

def get_main_follow_contract_table():
    contracts = Contract.objects.filter(is_deleted=False)
    row_list = []
    temp_list = []
    res_servs_name = []
    for contract in contracts:
        contract_serial       = contract.serialNum
        client_name         = contract.client.name
        client_phone        = contract.client.phone
        client_area         = contract.client.addressArea.name
        contract_services   = contract.services.all()
        for service in contract_services:
            res_servs_name.append(service.name)
        temp_list.append(contract_serial)
        temp_list.append(client_name)
        temp_list.append(client_phone)
        temp_list.append(client_area)
        temp_list.append(res_servs_name)
        row_list.append(temp_list)
        temp_list = []
        res_servs_name = []
    rows  = row_list
    data={"thead":  ["سريال التعاقد","اسم العميل","رقم الهاتف","المنطقة","الخدمات"],"rows":rows}
    return data

def get_main_follow_current_contract_table():
    contracts = Contract.objects.filter(is_deleted=False)
    row_list = []
    temp_list = []
    temp_list2 = []
    temp_list3 = []
    for contract in contracts:
        contract_serial       = contract.serialNum
        client_name         = contract.client.name
        client_phone        = contract.client.phone
        client_area         = contract.client.addressArea.name
        contract_services   = contract.services.all()
        for service in contract_services:
            service_name=service.name
            temp_list3.append(service_name)
            serviceCollcetStatusNumsRecord = FollowContractServices.objects.filter(is_deleted=False,service=service)
            temp_list3.append(serviceCollcetStatusNumsRecord[0].collcetStatusNums)
            temp_list2.append(temp_list3)
            temp_list3 = []
        temp_list.append(contract_serial)
        temp_list.append(client_name)
        temp_list.append(client_phone)
        temp_list.append(client_area)
        temp_list.append(temp_list2)
        row_list.append(temp_list)
        temp_list = []
        temp_list2 = []

    rows  = row_list
    data={"thead":  ["سريال التعاقد","اسم العميل","رقم الهاتف","المنطقة","الخدمات"],"rows":rows}
    return data

class follow_contract(APIView):
    def get(self, request):
        # try :
        table_type   = request.GET.get('table_type' , '0')
        if table_type != '0':
            if table_type == "main_table":
                data = get_main_follow_contract_table()
            elif table_type == "curent_table":
                data = get_main_follow_current_contract_table()
            else:
                data = {'erorr':f'table type {table_type} selected is not supported'}
        else:
            data = {'erorr':'not table type selected'}
        # except:
        #     data = {'erorr':'erorr occured here'}
        return Response(data)















