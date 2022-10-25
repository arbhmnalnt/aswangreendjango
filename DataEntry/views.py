from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import *
from django.core import serializers as core_serializers
from .serializers import ContractSerializer, ServiceSerializer, ClientSerializer

import datetime
from datetime import datetime
import json

# first make the authorizations
class addNewContract(APIView):
    def post(self, request):
        client_data_dict = {}
        data2=json.loads(request.body)
        newClientId  =  create_new_client(data2) # wikk be returened after inserting the new client
        # client contract data
        newContractId = create_new_contract(data2, newClientId)
        # follow Services
        make_new_contract_service_followers(data2, newContractId, newClientId)

        return Response({"msg": "done"})

class HandleClients(APIView):
    def get(self, request):
        # add all employess to client table for make them able to login
        # addEmployeesToClientTable()

        # # add missing info check to all Clients with missing info like:
        # # name is not length [complete name] ot missing serial num
        # # phone is not 11 digit length or missing area or missing details in address
        # checkmissingClientsInfo()
        return Response({"msg": "done"})

class filters(APIView):
    def get(self, request):
        data = {'status':'filter is working'}
        return Response(data)

class contractTables(APIView):
    def get(self, request):
            # try :
        tableType   = request.GET.get('tableType' , '0')
        if tableType != '0':
            if tableType == "currentContracts":
                data = currentContracts()
            elif tableType == "latestContracts":
                # data = latestTableTest()
                data = latestTable()

            elif tableType == "requiredOnContracts":
                data = requiredOnContracts()
            elif tableType == "fourth_table_type":
                data = fourth_table_function()
            elif tableType == "fifth_table_type":
                data = fifth_table_function()
            else:
                data = {'erorr':f'table type {tableType} selected is not supported'}
        else:
            data = {'erorr':'not table type selected'}
        # except:
        #     data = {'erorr':'erorr occured here'}
        return Response(data)

class getServices(APIView):
    def get(self, request):
        main_service   = Service.objects.all()
        simple_service = SimpleService.objects.all()
        services_list = []
        for service in main_service:
            service_dict = {}
            service_dict["label"] = service.name
            services_list.append(service_dict)
        for service in simple_service:
            service_dict = {}
            service_dict["label"] = service.name
            services_list.append(service_dict)
        return Response(services_list)

class getRegions(APIView):
    def get(self, request):
        areas = Area.objects.all()
        area_list = []
        area_dict2 = {}
        for area in areas:
            area_dict = {}
            area_dict["name"] = area.name
            area_dict["value"] = str(area.counter)
            area_list.append(area_dict)
        # data = {area_list}
        return Response(area_list)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test2(request):
    return HttpResponse("test")

####################  FUNCTIONS PART #################################
def make_new_contract_service_followers(data2, newContractId, newClientId):
    def get_month(date):
        # if day>25 and day>15: then maked the month is the next month else make it current month
        date_formatted = datetime.strptime(date, '%Y-%m-%d')
        if date_formatted.day > 15:
            if date_formatted.month != 12:
                month = date_formatted.month + 1
            else:
                month = 1
        return month
    client                  =   Client.objects.get(pk=newClientId)
    contract                =   Contract.objects.get(pk=newContractId)
    service_objects_list    =   data2["services"]
    for service in service_objects_list:
        service_self = Service.objects.get(pk=service["id"])

        follow_contract_services = FollowContractServices.objects.create(
            client=client, service=service_self, total_amount=service_self.price, remain_amount=service_self.price,
            collected_month=get_month(data2['date']),created_by=Employee.objects.get(pk=data2['userId'])
        )

        follow_contract_services.save()

def create_new_contract(data, newClientId):
    services_list = data["services"]
    services_id_list = []
    services_set = set()

    for service in services_list:
        serv = Service.objects.get(pk=service["id"])
        services_set.add(serv)

    contract = Contract.objects.create(
        serialNum=data["Serial"],client=Client.objects.get(pk=newClientId),belong_to=Employee.objects.get(pk=data['referer']),
        created_prev_date=data['date'],created_by=Employee.objects.get(pk=data['userId'])
    )
    contract.services.set(services_set)
    contract.save()
    contract_id = contract.id
    return contract_id

def create_new_client(dictt):
    client=Client.objects.create(
        name=dictt["name"],phone=dictt["phone"],nationalId=dictt["nationalId"], password="",
        serialNum=dictt["Serial"],area=Area.objects.filter(name=dictt["area"])[0],streetName=dictt["streetName"],addressBuilding=dict["addressBuilding"],
        addressApartment=dictt["addressApartment"],addressDetails=dictt["addressDetails"],created_prev_date=dictt["date"],
        created_by=Employee.objects.get(pk=dictt['userId'])
    )
    client.save()
    clientId=client.id
    return clientId


def currentContracts():
    list = ['تاريخ التعاقد','اسم العميل','رقم الهاتف','المنطقة','المسستحق','الخيارات']
    bigRows_list = []
    contracts = Contract.objects.all()
    big_list  = []
    for contract in contracts:
        total = 0
        row = ''
        small_list = []
        date = str(contract.created_at_date)
        client = contract.client
        clientName = contract.client.name
        clientId = contract.client.id
        clientArea = contract.client.area.name
        clientPhone = Client.objects.get(pk=clientId).phone
        follows = FollowContractServices.objects.filter(client=client)
        for follow in follows:
            total += follow.remain_amount

        row_dict = {"date":date,"clientId":clientId ,"clientName":{"value":clientName, "route":"viewClientBySerialNum"},"phone":clientPhone,
        "area":clientArea, "deserved": total}
        # small_list = ['date':]
        bigRows_list.append(row_dict)
    data = f"thead:{list}, rows:{bigRows_list}"
    return data

def addEmployeesToClientTable():
    employees = Employee.objects.all()
    for employe in employees:
        name     = employe.name
        phone    = employe.phone
        naId     = employe.naId
        Client.objects.create(name=name,phone=phone,nationalId=naId
        ,is_employee=True)

def checkmissingClientsInfo():
    clients = Client.objects.all()
    temp = 0
    for cl in clients:
        notes = ""
        cl.notes = ""
        cl.save()

        if cl.area or  cl.name or cl.password or  cl.serialNum or cl.nationalId or cl.phone == "-" or cl.area or cl.password or cl.name or  cl.serialNum or cl.nationalId or cl.phone is None or cl.area or cl.password  or cl.serialNum or cl.nationalId or cl.name  or cl.phone == "":
            temp += 1
            cl.missing_info = True
            if cl.area == "-" or cl.area is None or cl.area == "":
                notes += "المنطقة غير محددة\n"
            if cl.name == "-" or cl.name is None or cl.name == "":
                notes += "الإسم غير كامل أو غير مكتوب\n"
            if cl.serialNum == "-" or cl.serialNum is None or cl.serialNum == "":
                notes += "خطأ برقم السريال\n"
            if cl.nationalId == "-" or cl.nationalId is None or cl.nationalId == "" or len(str(cl.nationalId)) != 14:
                notes += "خطأ بالرقم القومى\n"
            if cl.phone == "-" or cl.name is None or cl.name == "" or len(str(cl.phone)) != 11:
                notes += "خطأ بالرقم التليفونى \n"
            if cl.password == "-" or cl.password is None or cl.password == "":
                notes += "كلمة السر فارغة"
            print(f'client id --> {cl.id} is missing area')
            cl.notes = notes
            print(f"client notes ==> {notes}")
            cl.save()
        else:
            continue
    print(f"total {temp} clients // done all clients check")