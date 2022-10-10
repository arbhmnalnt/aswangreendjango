from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from DataEntry.models import *
from django.core import serializers as core_serializers
from DataEntry.serializers import ContractSerializer, ServiceSerializer, ClientSerializer
from django.core.exceptions import ObjectDoesNotExist

# to get current month int
from datetime import datetime

current_month = int(datetime.now().month)

collection_day = 25

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def collectionDay(request):
    return HttpResponse(collection_day)



class addNewContract(APIView):
    def post(self, request):
        pass

# create
## APIView create operation
# class addClient(APIView):
#     def post(self, request):
#         serializer = ClientSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        follows =  FollowContractServices.objects.filter(collcetStatusNums='مطلوب الدفع',is_deleted=False)
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
        collectors = Employee.objects.filter(jobTitle="موظف تحصيل").count()
        data = {'currentClients': curr_count, 'remainingCollections': req_count, 'collected': coll_count, 'collectors':collectors}
        return Response(data)

def collect_statue(service,client, current_month):
    follow = FollowContractServices.objects.filter(client=client, service=service)[0]
    if follow.collected_month  < current_month-1:
        statue = "لم يتم التحصيل"
    elif follow.collected_month  == current_month:
        statue = 'مطلوب التحصيل'
    else:
        statue = 'متأخر'
    return statue

def get_main_follow_current_contract_table():
    start=20
    contracts = Contract.objects.filter(is_deleted=False)[:start]
    row_list = []
    temp_list = []
    res_servs_name = []
    late = False
    for contract in contracts:
        contract_serial       = contract.serialNum
        client               = contract.client
        client_name         = contract.client.name
        client_phone        = contract.client.phone
        client_area         = contract.client.addressArea.name
        contract_services   = contract.services.all()
        for service in contract_services:
            res_servs_name.append(service.name)
            collectStatue = collect_statue(service, client, current_month+1)
        temp_list.append(contract_serial)
        temp_list.append(client_name)
        temp_list.append(client_phone)
        temp_list.append(client_area)
        temp_list.append(res_servs_name)
        temp_list.append(collectStatue)
        row_list.append(temp_list)

        temp_list = []
        res_servs_name = []
    rows  = row_list
    data={"thead":  ["سريال التعاقد","اسم العميل","رقم الهاتف","المنطقة","الخدمات","حالة التحصيل","سريال الفاتورة"],"rows":rows}
    return data

def latestTable():
    contracts = Contract.objects.filter(is_deleted=False)[:20]
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

# class contractTables(APIView):
#     def get(self, request):
#         # try :
#         tableType   = request.GET.get('tableType' , '0')
#         if tableType != '0':
#             if tableType == "currentContracts":
#                 data = get_main_follow_current_contract_table()
#             elif tableType == "latestContracts":
#                 data = latestTable()

#             elif tableType == "third_table_type":
#                 data = third_table_function()
#             elif tableType == "fourth_table_type":
#                 data = fourth_table_function()
#             elif tableType == "fifth_table_type":
#                 data = fifth_table_function()
#             else:
#                 data = {'erorr':f'table type {table_type} selected is not supported'}
#         else:
#             data = {'erorr':'not table type selected'}
#         # except:
#         #     data = {'erorr':'erorr occured here'}
#         return Response(data)

#for testing
class collectionStatsTest(APIView):
    def get(self, request):
        data ={"currentClients": 1200, "remainingCollections": 200, "collected": 1000, "collectors": 5}
        return Response(data)

def currentContractsTest():
    rows = [ "32", "على حسن على", "01012355695", "المقاولون", "جمع منزلى", "مطلوب التحصيل", "8965" ], [ "1", "ايمن محمد السيد", "01554899523", "المحمودية", "نظافة داخلى ", "شتم التحصيل", "9856" ], [ "321", "على أبو العينين محمد", "01155322892", "العقاد", "رش وتعقيم", "تم التحصيل", "8564" ], [ "231", "مصطفى محمد السعيد", "01254886231", "عمائر الاستاد", "جمع منزلى", "تم التحصيل", "4565" ], [ "56", "محمدين على هاشم", "01145888752", "عمائر التأمين الصحى", "جمع منزلى ", "مطلوب التحصيل", "2345" ], [ "98", "محمود السيد بكرى", "01054684565", "المقاولون", "نظافة داخلى ", "مطلوب التحصيل", "4785" ], [ "12", "سيد على محمد", "01078953322", "المحمودية", "رش وتعقيم", "مطلوب التحصيل", "9855" ], [ "45", "حسن محمد مصطفى", "01568756523", "العقاد", "جمع منزلى", "مطلوب التحصيل", "7412" ], [ "65", "محمود حسين السيد", "01265498566", "المقاولون", "نظافة داخلى ", "متأخر", "9632" ], [ "89", "على محمد مختار", "01287986645", "المحمودية", "رش وتعقيم", "تم التحصيل", "8526" ], [ "78", "ايمن طه عبد الكريم", "01256849874", "العقاد", "جمع منزلى", "متأخر", "4587" ], [ "12", "محمد عبد الرحيم على", "01005464684", "المقاولون", "جمع منزلى ", "تم التحصيل", "6589" ]
    data={"thead":  ["سريال التعاقد","اسم العميل","رقم الهاتف","المنطقة","الخدمات","حالة التحصيل","سريال الفاتورة"],"rows":rows}
    return data

def latestTableTest():
    rows = ["25135","احمد حسن محمد","01145955231","العقاد","جمع منزلى",]
    data={"thead":  ["سريال التعاقد","اسم العميل","رقم الهاتف","المنطقة","الخدمات"],"rows":rows}
    return data

import json
class authUser(APIView):
    def post(self, request):
        # request.POST['title']
        data = json.loads(request.body)
        username = data["email"]
        password = data["password"]

        if username == "dataentry@aswangreen.it":
            data = {"isAuthenticated": True, "role": "dataEntry","name": "جمال كامل عبدالله" ,"job": "ادخال بيانات والتحصيل"}
        else:
            data = {"isAuthenticated": False, "email":username}
        return Response(data)

def requiredOnContracts():
    # rows = [] [{ "32", "على حسن على", "01012355695", "المقاولون", "2022-05-10", "المقاولون امام جرجاج شركة المقاولون العرب - عمارة 3 - شقه 3 بالدور الثانى", "110" ], [ "1", "ايمن محمد السيد", "01554899523", "المحمودية", "2022-05-11", "المحمودية بجوار البنزينة - عمارة 15 - شقه 2 - الدور الارضى", "0" ], [ "321", "على أبو العينين محمد", "01155322892", "العقاد", "2022-05-12", "العقاد بجوار مقهى العندليب - عمارة 2 - شقه 6 الدور الثالث", "0" ], [ "231", "مصطفى محمد السعيد", "01254886231", "عمائر الاستاد", "2022-05-13", "عماره 5 - شقه 4 - الدور الثانى", "0" ], [ "56", "محمدين على هاشم", "01145888752", "عمائر التأمين الصحى", "2022-05-14", "عماره 17 شقه 8 - الدور الرابع", "50" ], [ "98", "محمود السيد بكرى", "01054684565", "المقاولون", "2022-05-15", "عماره 6 - شقه 5 - الدور الثالث", "30" ], [ "12", "سيد على محمد", "01078953322", "المحمودية", "2022-05-16", "عماره 3 شقه 1 - الدور الارضى", "160" ], [ "45", "حسن محمد مصطفى", "01568756523", "العقاد", "2022-05-17", "عماره 9 شقه 3 الدور الثانى", "0" ], [ "65", "محمود حسين السيد", "01265498566", "المقاولون", "2022-05-18", "عماره 11 شقه 4 الدور الثانى", "100" ], [ "89", "على محمد مختار", "01287986645", "المحمودية", "2022-05-19", "عماره 13 - شقه 5 - الدور الثالث", "0" ], [ "78", "ايمن طه عبد الكريم", "01256849874", "العقاد", "2022-05-20", "عماره 7 - شقه 3 - الدور الثانى", "150" ], [ "12", "محمد عبد الرحيم على", "01005464684", "المقاولون", "2022-05-21", "عماره 12 - شقه 4 - الدور الثانى", "0" ][ "32", "على حسن على", "01012355695", "المقاولون", "2022-05-10", "المقاولون امام جرجاج شركة المقاولون العرب - عمارة 3 - شقه 3 بالدور الثانى", "110" ], [ "1", "ايمن محمد السيد", "01554899523", "المحمودية", "2022-05-11", "المحمودية بجوار البنزينة - عمارة 15 - شقه 2 - الدور الارضى", "0" ], [ "321", "على أبو العينين محمد", "01155322892", "العقاد", "2022-05-12", "العقاد بجوار مقهى العندليب - عمارة 2 - شقه 6 الدور الثالث", "0" ], [ "231", "مصطفى محمد السعيد", "01254886231", "عمائر الاستاد", "2022-05-13", "عماره 5 - شقه 4 - الدور الثانى", "0" ], [ "56", "محمدين على هاشم", "01145888752", "عمائر التأمين الصحى", "2022-05-14", "عماره 17 شقه 8 - الدور الرابع", "50" ], [ "98", "محمود السيد بكرى", "01054684565", "المقاولون", "2022-05-15", "عماره 6 - شقه 5 - الدور الثالث", "30" ], [ "12", "سيد على محمد", "01078953322", "المحمودية", "2022-05-16", "عماره 3 شقه 1 - الدور الارضى", "160" ], [ "45", "حسن محمد مصطفى", "01568756523", "العقاد", "2022-05-17", "عماره 9 شقه 3 الدور الثانى", "0" ], [ "65", "محمود حسين السيد", "01265498566","zالمقاولون", "2022-05-18", "عماره 11 شقه 4 الدور الثانى", "100" ], [ "89", "على محمد مختار", "01287986645", "المحمودية", "2022-05-19", "عماره 13 - شقه 5 - الدور الثالث", "0" ], [ "78", "ايمن طه عبد الكريم", "01256849874", "العقاد", "2022-05a-20", "عماره 7 - شقه 3 - الدور الثانى", "150" ], [ "12", "محمد عبد الرحيم على", "01005464684", "المقاولون", "2022-05-21", "عماره 12 - شقه 4 - الد
    #""ور الثانى", "0"

    rows =[]
    data = {"thead": ["سريال التعاقد","اسم العميل ","رقم الهاتف","المنطقة","تاريخ التعاقد","العنوان بالتفصيل","المستحق","الملاحظات"
  ],"rows": rows}
    return data

class contractTables(APIView):
    def get(self, request):
            # try :
        tableType   = request.GET.get('tableType' , '0')
        if tableType != '0':
            if tableType == "currentContracts":
                # data = get_main_follow_current_contract_table()
                data = currentContractsTest()
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
















