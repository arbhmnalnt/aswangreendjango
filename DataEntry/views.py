from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import *
from django.core import serializers as core_serializers
from .serializers import ContractSerializer, ServiceSerializer, ClientSerializer
import json


class HandleClients(APIView):
    def get(self, request):
        # add all employess to client table for make them able to login 
        # addEmployeesToClientTable()

        # add missing info check to all Clients with missing info like:
        # name is not length [complete name] ot missing serial num
        # phone is not 11 digit length or missing area or missing details in address
        checkmissingClientsInfo()
        return Response({"msg": "done"})

# first make the authorizations
class addNewContract(APIView):
    def get(self, request):
        data2=json.loads(request.body)
        clientName           = data2["clientName"]
        clientPhone          = data2["clientPhone"]
        clientArea           = data2["clientArea"]
        clientAddressDetails = data2["clientAddressDetails"]
        clientBuilding       = data2["clientBuilding"]
        clientApartment      = data2["clientApartment"]
        ClientReferer        = data2["ClientReferer"]
        clientServices       = data2["clientServices"]
        contractSerial       = data2["contractSerial"]
        contractDate         = data2["contractDate"]
        created_by           = Client.objects.filter(is_employee=True,name="فيرا").first()
        addNewAll = {clientName,clientPhone,clientArea,clientAddressDetails,clientBuilding,clientApartment,ClientReferer,clientServices,
        contractSerial,contractDate}
        data = {'status','done'}
        return Response(data)


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


####################  FUNCTIONS PART #################################3
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


# "thead": [
#     "تاريخ التعاقد",
#     "اسم العميل",
#     "رقم الهاتف",
#     "المنطقة",
#     "المستحق",
#     "الخيارات"
#   ],
# "rows": [
#     {
#       "date": "12/2/2022",
#       "clientName": {
#         "value": "محمد حسين",
#         "route": ""
#       },
#       "phone": "01233326751",
#       "area": "العقاد",
#       "المستحق": 1200,
#       "nestedTable": {
#         "thead": [
#           "تاريخ التعاقد",
#           "اسم العميل",
#           "رقم الهاتف",
#           "المنطقة",
#           "المستحق"
#         ],
#         "rows": [
#           {
#             "date": "12/2/2022",
#             "clientName": {
#               "value": "محمد حسين",
#               "route": ""
#             },
#             "phone": "01233326751",
#             "area": "العقاد",
#             "المستحق": 1200
#           }
#         ]
#       }
#     }
#   ]
