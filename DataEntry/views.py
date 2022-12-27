from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status as st
from .models import *
from django.core import serializers as core_serializers
from .serializers import ContractSerializer, ServiceSerializer, ClientSerializer
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required

today = datetime.now()

todayDate = datetime.today().strftime("%Y-%m-%d")  #this is used in the page

todayUser = datetime.today().strftime("%d-%m-%Y")
month = today.month

@api_view(['GET'])
def checkClientSerial(request):
    frontSerial   = request.GET.get('serial')
    res = False
    frontSerialExist = Client.objects.filter(serialNum=frontSerial).count()
    if frontSerialExist > 0:
        res = "found"
    else:
        res = "not found"
    data = {'responseText':res}
    return Response(data)

def TnewContract(request):
    services  = Service.objects.all()
    servicesList = ["service-"+str(service.id) for service in services]
    temp = True
    print(f"here => 04")
    continueContracts = getUnfinishedClients(temp)
    print(f"continueContracts => {continueContracts}")
    if request.method == 'POST':
        date            = request.POST['date']    # todayUser
        userId          = request.POST['userId']
        serial          = request.POST['serial']
        clientName      = request.POST['name']
        phone           = request.POST['phone']
        area            = Area.objects.get(pk=request.POST['area'])
        addressDetails  = request.POST['addressDetails']
        apartment       = isEmptyStr(request.POST['apartment'])
        print(f"addressBuilding => {apartment}")
        flat            = isEmptyStr(request.POST['float'])
        servicesIdsList = request.POST['servicesId']
        servicesIdsList = servicesIdsList.split(',')
        servicesIdsListint = [int(s) for s in servicesIdsList]
        referer         = 0 if request.POST['referer'] == '0' else Employee.objects.get(pk=request.POST['referer'])
        clientServicesList = [Service.objects.get(pk=service) for service in servicesIdsListint ]
        belong_to      = Employee.objects.get(pk=referer) if referer != 0 else ''
        ##########

        # to be done
        data2 = {"name":clientName, "phone":phone, "nationalId":"", "Serial":serial, "area":area, "streetName":addressDetails,
        "addressBuilding":apartment,"addressApartment": flat, "addressDetails": f" {addressDetails} - {apartment} - {flat}",
        "services":servicesIdsListint,"referer":referer,"date":date,"userId":userId}


        newClientId  =  create_new_client(data2) # wikk be returened after inserting the new client
        # client contract data
        newContractId = create_new_contract(data2, newClientId)
        # follow Services
        make_new_contract_service_followers(data2, newContractId, newClientId)
        return redirect('/DataEntry/')
    else:
        pass
    areas     = Area.objects.all()
    employees = Employee.objects.all()
    ctx={'services':services, 'employees':employees, 'areas':areas,'today':todayDate,
    'todayUser':todayUser, 'contracts':continueContracts}
    return render(request, 'DataEntry/TnewContract.html', ctx)

@login_required
def TmainPage(request):
    # stats part
    remainingCollections = len(peopleTocollectFrom())
    collected            = len(peopleCollectedFrom())
    currentClients       = Contract.objects.all().count()
    collectorsNum        = Employee.objects.filter(jobTitle="موظف تحصيل").count()
    # latest contracts
    contracts            = Contract.objects.all().order_by('-id')[:20]
    # current collecr orders
    orders               = CollectOrder.objects.filter(month=month)
    ctx= {'remainingCollections':remainingCollections, "collected":collected, "currentClients":currentClients, "collectorsNum":collectorsNum,
        'items':contracts, 'contractsLen':contracts.count(), 'orders':orders, 'ordersLen':orders.count()}

    return render(request, 'DataEntry/TmainPage.html', ctx)

# tableTypes  [detailed,2,3]
class generateFilteredTableView(APIView):
    def get(self, request):
        filterKeysDict=json.loads(request.body)
        tableType = "detailed"
        contracts = filterFollowContractServicesRecord(filterKeysDict)
        print(f"contracts => {contracts}")
        data = generateTable(contracts, tableType)
        return Response(data)

class newCollectOrder(APIView):   # this class used with new collect orders also to update current collect orders
    def post(self, request):
        data2=json.loads(request.body)
        collectorId = data2["collectorId"]
        collector = Employee.objects.get(pk=collectorId)
        clients_set = manyToManyIdSave(data2["clients"], Client)
        areas_set = manyToManyIdSave(data2["areas"], Area)
        month = data2["month"]
        required = data2["required"]
        if 'collectOrderID' in data2:
            idd = data2["collectOrderID"]
            collectOrder = CollectOrder.objects.filter(pk=idd)
            collectOrder.update(collector=collector,month=month, required=required)
            collectOrder[0].clients.set(clients_set)
            collectOrder[0].areas.set(areas_set)
            collect_order_id = collectOrder[0].id
        else:
            collect_order = CollectOrder.objects.create(collector=collector,month=month, required=required)
            collect_order.clients.set(clients_set)
            collect_order.areas.set(areas_set)
            collect_order_id = collect_order.id
        data = {'msg':'done', 'collectOrderId':collect_order_id}
        return Response(data)

class UnPaidClientsTable(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        dataList = []
        page = int(data2["page"])
        basic_start = 0
        basic_end = 20
        start = (page-1)*basic_end
        end = basic_end*page
        contract_list = []
        contract_list2 = []
        follows = FollowContractServices.objects.filter(collcetStatusNums="مطلوب الدفع")
        for follow in follows:
            contract_list2.append(Contract.objects.get(client=follow.client))
        count = len(contract_list2)
        if count > 0:
            contracts = [c for c in contract_list2 if  c in Contract.objects.all().order_by('-id')[start:end]]
            for contract in contracts:
                if contract in contract_list:
                    continue
                else:
                    contract_list.append(contract)
            print(f"contracts => {contract_list}")
            thead = {"contractSerial":"سريال الفاتورة","contractDate":"تاريخ التعاقد",
            "clientName":"اسم العميل","phone":"رقم الهاتف","area":"المنطقة",
            "addressDetails":"العنوان بالتفصيل", "deserved":"المستحق", "notes":"الملاحظات"}
            for contract in contract_list:
                temp = {}
                temp["contractId"]     = contract.id
                temp["contractSerial"] = contract.serialNum
                temp["clientName"]     = contract.client.name
                temp["phone"]          = contract.client.phone
                temp["addressDetails"] = contract.client.addressDetails
                temp["area"]           = contract.client.area.name
                # follows = FollowContractServices.objects.filter(client=contract.client)
                temp["deserved"]  = contract.client.deserved
                temp["notes"]     = contract.client.notes
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList, 'start':start, 'end':end}
        else:
            data = {}
        data = data
        return Response(data)

class getUnPaidClientsNum(APIView):
    def get(self, request):
        data = {'unPaidClientsNum': len(peopleTocollectFrom())}
        return Response(data)

class currentContractTableViewClientProfile(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        clientId = int(data2["clientId"])
        data = getClientProfileData(clientId)
        return Response(data)


class currentContractTableEditContrctServices(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        contract_id = int(data2["contractId"])
        updateFollowContractServices(data2,update_contract(data2, contract_id))
        data = {"msg":"done"}
        return Response(data)

class currentContractTable(APIView):
    def post(self, request):
        dataList = []
        data2=json.loads(request.body)
        page = int(data2["page"])
        basic_start = 0
        basic_end = 20
        start = (page-1)*basic_end
        end = basic_end*page
        count = Contract.objects.all().count()
        if count > 0:
            contracts=Contract.objects.all().order_by('-id')[start:end]
            thead = {"contractSerial":"سريال الفاتورة", "clientName":"اسم العميل","phone":"رقم الهاتف","area":"المنطقة",
                    "services":"الخدمات", "collectStatus":"حالة التحصيل", "billSerial":"سريال الفاتورة"}
            for contract in contracts:
                temp = {}
                temp["contractId"]     = contract.id
                temp["contractSerial"] = contract.serialNum
                temp["clientName"]     = contract.client.name
                temp["phone"]          = contract.client.phone
                temp["services"]       = [service.name for service in contract.services.all()]
                temp["area"]           = contract.client.area.name
                follows = FollowContractServices.objects.filter(client=contract.client)
                temp["collectStatus"]  = getCollectStatus(follows)
                temp["billSerial"]     = "004592"
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList, 'start':start, 'end':end}
        else:
            data = {}
        return Response(data)

class currentContractCount(APIView):
    def get(self, request):
        data = Contract.objects.count()
        return Response(data)

class missingOrUnfinishedRequests(APIView):
    def get(self, request):
        temp=False
        data3 = getUnfinishedClients(temp)
        return Response(data3)


class mainPageStatsThird(APIView):
    def get(self, request):
        dataList = []
        count = Contract.objects.all().count()
        if count > 0:
            contracts=Contract.objects.all().order_by('-id')[:20]
            thead = {"contractSerial":"سريال الفاتورة", "clientName":"اسم العميل","phone":"رقم الهاتف","area":"المنطقة","services":"الخدمات"}
            for contract in contracts:
                temp = {}
                temp["contractSerial"] = contract.serialNum
                temp["clientName"]   = contract.client.name
                temp["phone"]        = contract.client.phone
                temp["services"]     = [service.name for service in contract.services.all()]
                temp["area"]         = contract.client.area.name
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList}
        else:
            data = {}
        return Response(data)


# start main page apis
class mainPageStatsSecond(APIView):
    # طلبات التحصيل الحالية
    def get(self, request):
        is_orders = CollectOrder.objects.filter(month=month).count()
        dataList = []
        if is_orders >0:
            orders = CollectOrder.objects.filter(month=month)
            for order in orders:
                temp = {}
                temp["collector"] = order.collector.name
                temp["clientsNum"]= order.clients.count()
                temp["areas"]     = [area.name for area in order.areas.all()]
                temp["date"]      = order.created_at_date
                dataList.append(temp)
            data = dataList
        else:
            data = {}
        return Response(data)


class mainPageStatsFirst(APIView):
    def get(self, request):
        data = {"remainingCollections":len(peopleTocollectFrom()), "collected":len(peopleCollectedFrom()), "currentClients":Contract.objects.all().count(),
        "collectorsNum":Employee.objects.filter(jobTitle="موظف تحصيل").count()}
        return Response(data)
# end of main page apis

# first make the authorizations
class addNewContract(APIView):
    def post(self, request):
        client_data_dict = {}
        data2=json.loads(request.body)
        if 'id' in data2:
            updateClientId  =  update_client_data(data2)
            newContractId = create_new_contract(data2, updateClientId)
            make_new_contract_service_followers(data2, newContractId, updateClientId)
            return Response({"msg": "done"})
        else:
           pass
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
        checkmissingClientsInfo()
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
#==================================================================================================================================
####################################################  FUNCTIONS PART #######################################################
#==================================================================================================================================
def isEmptyStr(string):
    res = ""
    if len(string) > 0:
        res = string
    else:
        res = ""
    return res

def generateTable(contracts, tableType):
    contract_list = contracts
    dataList = []
    thead = {"contractSerial":"سريال الفاتورة","contractDate":"تاريخ التعاقد",
            "clientName":"اسم العميل","phone":"رقم الهاتف","area":"المنطقة",
            "addressDetails":"العنوان بالتفصيل", "deserved":"المستحق", "notes":"الملاحظات"}
    print(f"contract_list => {contract_list}")
    if contract_list == None:
        dataList = ''
    else:
        for contracts in contract_list:
            if contracts == '':
                continue
            else:
                pass
            temp = {}
            temp["contractId"]     = contracts.id
            temp["contractSerial"] = contracts.serialNum
            temp["clientName"]     = contracts.client.name
            temp["phone"]          = contracts.client.phone
            temp["addressDetails"] = contracts.client.addressDetails
            temp["area"]           = contracts.client.area.name
            # follows = FollowContractServices.objects.filter(client=contracts.client)
            temp["deserved"]  = contracts.client.deserved
            temp["notes"]     = contracts.client.notes
            dataList.append(temp)
    table = {"thead":thead, "rows":dataList}
    #return table
    # testing
    return table

def set_follow_areas_name(follows):
    for follow in follows:
        FollowContractServices.objects.filter(pk=follow.id).update(area=follow.client.area.name)


set_follow_areas_name(FollowContractServices.objects.all())

#@csrf_exempt
def filterFollowContractServicesRecord(filterKeysDictRequest):
    # filterKeysDictRequest = {'page':'2','area':'الإسكان المميز'}
    # filterKeysArray may contain (client, serviceCollectDayStart, serviceCollectDayEnd
    #  collected_month, remain_amount, area, collcetStatusNums)  collcetStatusNums # حالة الدفع
    res_follows = 0
    print(f"filterKeysDictRequest keys is => {filterKeysDictRequest.keys}")
    for key in filterKeysDictRequest:
        res_follows = FollowContractServices.objects.filter(**filterKeysDictRequest)
    if res_follows == 0:
        uniqueContracts = ['']
        # print(f"res_follows => here 4")
        # print(f"res_follows => {res_follows}")
    else:
        # print(f"here 5")
        # print(f"res_follows => {res_follows}")
        contarcts = [Contract.objects.get(client=follow.client) for follow in res_follows]
        uniqueContracts = list(set(contarcts))
    return uniqueContracts
    # for testing  only  (res_follows[0])
    # return HttpResponse(uniqueContracts)


# def recordManage(request):
#     month = datetime.now().month
#     print("month => ", month)

#     ctx = {'month':month}
#     return render(request, 'clinics/record_management.html', ctx)

def manyToManyIdSave(manyToManyList,manyTomanyTable):
    manyToManySet = set()
    for objectID in manyToManyList:
        manyToManyObject = manyTomanyTable.objects.get(pk=objectID)
        manyToManySet.add(manyToManyObject)
    return manyToManySet

def getClientProfileData(clientId):
    client = Client.objects.get(pk=clientId)
    contract = Contract.objects.get(client=client)
    clientServices = [service.name for service in contract.services.all()]
    data = {'clientName':client.name, 'phone':client.phone, 'area':client.area.name,
        'addressDetails':client.addressDetails, 'services':clientServices, 'contractSerial':contract.serialNum,
        'contractDate':contract.created_at_date, 'collectionStatus':"تم التحصيل", 'deserved':"0"}
    return data

# def update_contract(data, clientId):
def updateFollowContractServices(data2,contractId):
    def get_month(date):
        # if day>25 and day>15: then maked the month is the next month else make it current month
        date_formatted = datetime.strptime(date, '%Y-%m-%d')
        month = 0
        if date_formatted.day > 15:
            if date_formatted.month != 12:
                month = date_formatted.month + 1
            else:
                month = 1
        else:
            month = date_formatted.month
        return month
    contract                =   Contract.objects.get(pk=contractId)
    contractDate            =   contract.created_prev_date
    service_objects_list    =   data2["services"]
    current_services_list   =   contract.sevices
    services_list=[]
    for i in service_objects_list:
        for j in current_services_list:
            if(j.find(i)!=-1 and j not in services_list):
                services_list.append(j)

    print(f"services_list =>  {services_list}")
    for service in services_list:
        service_self = Service.objects.get(pk=service)

        follow_contract_services = FollowContractServices.objects.create(area=contract.area.name,
            service=service_self, startingDate=contractDate,total_amount=service_self.price, remain_amount=service_self.price,
            collected_month=get_month(data2['date']),created_by=Employee.objects.get(pk=data2['userId'])
        )

        follow_contract_services.save()


def update_contract(data, contractID):
    services_list = data["services"]
    services_id_list = []
    services_set = set()
    i = 0
    for service in services_list:
        serv = Service.objects.get(pk=service)
        services_set.add(serv)
        i += 1

    contract = Contract.objects.get(pk=contractID)
    contract.services.set(services_set)
    contract.save()
    contract_id = contract.id
    return contract_id

def getCollectStatus(follows):
    status = "تم التحصيل"
    for follow in follows:
        if follow.collcetStatusNums == "مطلوب الدفع":
            status = "مطلوب الدفع"
            break
    return status

def clientRequestContact(client):
    cond = False
    if client.activation_request:
        cond =  True
    return cond

def getUnfinishedClients(cond):
    clients = Client.objects.all()
    UnclientList = []
    clintRecords = []
    for client in clients:
        temp = {}
        if clientMissingInfo(client) or clientRequestContact(client):
            print(f"client missing info {client.id} == > {client.name}")
            clintRecords.append(client)
            temp["id"] = client.id
            temp["name"] = client.name
            temp["phone"] = client.serialNum
            temp["address"] = client.addressDetails
            temp["serialNum"] = client.serialNum
            temp["referrer"] = client.belongs_to
            temp["services"] = []
            UnclientList.append(temp)
        else:
            pass
            #print(f"client good info {client.id} == > {client.name}")
    data = UnclientList
    if cond :
        data = clintRecords
        return data
    else:

        print("finished looping")
        return data

def clientMissingInfo(cl):
    cond = False
    if cl.area or cl.name  or cl.serialNum or cl.nationalId or cl.phone == "-" or cl.area or cl.name or  cl.serialNum or cl.nationalId or cl.phone is None or cl.area or cl.serialNum or cl.nationalId or cl.name  or cl.phone == "":
        cond = True
    else:
        cond = False
    return cond

def clientRequest(client):
    cond = False
    return cond

def peopleCollectedFrom():
    names_list = []
    follows = FollowContractServices.objects.filter(collcetStatusNums="تم الدفع")
    print(f"follows => {follows}")
    for follow in follows:
        client = follow.client
        is_count = FollowContractServices.objects.filter(client=client,collcetStatusNums="مطلوب الدفع").count()
        if is_count == 0:
            names_list.append(follow.client.name)
        else:
            pass
    client_names =  sorted(set(names_list))
    return client_names

def peopleTocollectFrom():
    names_list = []
    follows = FollowContractServices.objects.filter(collcetStatusNums="مطلوب الدفع")
    for follow in follows:
        names_list.append(follow.client.name)
    client_names =  sorted(set(names_list))
    return client_names

def make_new_contract_service_followers(data2, newContractId, newClientId):
    def get_month(date):
        # if day>25 and day>15: then maked the month is the next month else make it current month
        date_formatted = datetime.strptime(date, '%Y-%m-%d')
        if date_formatted.day > 15:
            if date_formatted.month != 12:
                month = date_formatted.month + 1
            else:
                month = 1
        else:
            month = date_formatted.month
        print(f"this month is {month}")
        return month

    client                  =   Client.objects.get(pk=newClientId)
    contract                =   Contract.objects.get(pk=newContractId)
    service_objects_list    =   data2["services"]
    for service in service_objects_list:
        service_self = Service.objects.get(pk=service)

        follow_contract_services = FollowContractServices.objects.create(
            client=client, service=service_self, total_amount=service_self.price, remain_amount=service_self.price,
            collected_month=get_month(data2['date']),created_by=Employee.objects.get(pk=data2['userId'])
        )

        follow_contract_services.save()

def create_new_contract(data, newClientId):
    services_list = data["services"]
    services_id_list = []
    services_set = set()
    i = 0
    for service in services_list:
        serv = Service.objects.get(pk=service)
        services_set.add(serv)
        i += 1

    contract = Contract.objects.create(
        serialNum=data["Serial"],client=Client.objects.get(pk=newClientId),
        belong_to=Employee.objects.get(pk=data['referer'] if data['referer'] != 0 else 10),
        created_prev_date=data['date'],created_by=Employee.objects.get(pk=data['userId'])
    )
    contract.services.set(services_set)
    contract.save()
    contract_id = contract.id
    return contract_id

def update_client_data(dictt):
    # Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
    clientId = dictt["id"]
    client = Client.objects.filter(pk=clientId)
    client.update(
        name=dictt["name"],phone=dictt["phone"],nationalId=dictt["nationalId"], password="",
        serialNum=dictt["Serial"],area=Area.objects.filter(name=dictt["area"])[0],streetName=dictt["streetName"],addressBuilding=dictt["addressBuilding"],
        addressApartment=dictt["addressApartment"],addressDetails=dictt["addressDetails"],created_prev_date=dictt["date"],
        created_by=Employee.objects.get(pk=dictt['userId'])
        )
    return clientId

def create_new_client(dictt):

    client=Client.objects.create(
        name=dictt["name"],phone=dictt["phone"],nationalId=dictt["nationalId"], password="",
        serialNum=dictt["Serial"],area=Area.objects.filter(name=dictt["area"])[0],streetName=dictt["streetName"],
        addressBuilding=dictt["addressBuilding"],addressApartment=dictt["addressApartment"],addressDetails=dictt["addressDetails"],
        created_prev_date=dictt["date"],created_by=Employee.objects.get(pk=dictt['userId'])
    )
    client.save()
    clientId=client.id
    return clientId


def currentContracts():
    list = ['تاريخ التعاقد','اسم العميل','رقم الهاتف','المنطقة','المستحق','الخيارات']
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

        if cl.area or  cl.name or cl.password or  cl.serialNum or cl.phone == "-" or cl.area or cl.password or cl.name or  cl.serialNum  or cl.phone is None or cl.area or cl.password  or cl.serialNum or cl.nationalId or cl.name  or cl.phone == "":
            temp += 1
            cl.missing_info = True
            if cl.area == "-" or cl.area is None or cl.area == "":
                notes += "المنطقة غير محددة\n"
            if cl.name == "-" or cl.name is None or cl.name == "":
                notes += "الإسم غير كامل أو غير مكتوب\n"
            if cl.serialNum == "-" or cl.serialNum is None or cl.serialNum == "":
                notes += "خطأ برقم السريال\n"
            if cl.phone == "-" or cl.name is None or cl.name == "" or len(str(cl.phone)) != 11:
                notes += "خطأ بالرقم التليفونى \n"
            print(f'client id --> {cl.id} is missing area')
            cl.notes = notes
            print(f"client notes ==> {notes}")
            cl.save()
        else:
            continue
    print(f"total {temp} clients // done all clients check")