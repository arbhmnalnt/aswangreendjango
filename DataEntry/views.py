from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import viewsets, status as st
from .models import *
from django.core import serializers as core_serializers
from .serializers import ContractSerializer, ServiceSerializer, ClientSerializer
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views import View
from django.db.models import Sum
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone


#
today = datetime.now()
todayDate = datetime.today().strftime("%Y-%m-%d")  #this is used in the page
todayUser = datetime.today().strftime("%d-%m-%Y")
month = today.month
    
@login_required
def TallContracts(request):
    listcount = 15
    # contracts_list = Contract.objects.filter(is_deleted=False, is_test=False)
    contracts_list = Contract.objects.filter(is_deleted=False)
    query       = request.GET.get('q')
    queryDate   = request.GET.get('qd')
    queryStatue = request.GET.get('qs')
    if query:
        contracts_list = Contract.objects.filter(
            Q(client__serialNum__icontains=query)& Q(is_deleted=False) |
            Q(client__name__icontains=query)& Q(is_deleted=False) |  Q(client__area__name__icontains=query)& Q(is_deleted=False)|
            Q(belong_to__name__icontains=query)& Q(is_deleted=False) |Q(client__customFilter__icontains=query)& Q(is_deleted=False)|
            Q(notes__icontains=query)& Q(is_deleted=False) |Q(created_by__name__icontains=query)& Q(is_deleted=False)|
            Q(services__name__icontains=query)& Q(is_deleted=False)
        ).distinct()
    if queryDate:
        contracts_list = Contract.objects.filter(created_prev_date=queryDate,is_deleted=False).distinct()

    paginator = Paginator(contracts_list, listcount) # 6 posts per page
    page = request.GET.get('page')
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)

    ctx = {'contracts_list':contracts_list, 'contracts':contracts}
    return render(request, 'Tahseal/TCurrentContract.html', ctx)


class CollectOrderList(ListView):
    model = CollectOrder
    template_name = "DataEntry/collect_order_list.html"
    context_object_name = "collect_orders"

class CollectOrderDetail(DetailView):
    model = CollectOrder
    template_name = "DataEntry/collect_order_detail.html"
    context_object_name = "collect_order"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the pk value from the URL
        pk = self.kwargs['pk']
        clients = CollectOrder.objects.get(pk=pk).clients.all()
        context['clients']   = clients
        contracts = []
        for client in clients:
            contracts.extend(Contract.objects.filter(client=client))
        context['contracts'] = contracts
        return context

class CollectOrderUpdate(UpdateView):
    model = CollectOrder
    template_name = "DataEntry/collect_order_update.html"
    fields = ['collector', 'clients', 'areas', 'month', 'confirmed', 'reason', 'required', 'created_prev_date', 'is_test']
    success_url = reverse_lazy('TcurrentCollectOrder')

class createNewCollectOrder(APIView):
    def post(self, request):
        data = request.POST
        values = {}
        for key, value in data.items():
             values[key] = value
        collectorId = values['collector']
        collectRecordSerial      = values['firstRecordSerial']
        collectRecordreceiptNum  = values['receiptsNum']
        print(f"collect record serial =>  {collectRecordSerial} // collect order reciept nums => {collectRecordreceiptNum}")
        collector = Employee.objects.get(pk=collectorId)
        values['collector'] = collector
        keys_only_dict = values.keys()
        print()
        clients = []
        for contractId in keys_only_dict:
            if contractId.isdigit():
                try:
                    # try to get a client with the given key
                    # client_record = Client.objects.get(pk=client)
                    client = Contract.objects.get(pk=contractId).client_id
                    clients.append(client)
                except Client.DoesNotExist:
                    # client does not exist, do nothing
                    pass
        for client in clients:
            follow_contracts = FollowContractServices.objects.filter(client__id=client).update(collcetStatus='pip')

        print(f"follow_contracts => {follow_contracts} because of clients ids => {clients}")
        areas = [Client.objects.get(pk=client).area.id  for client in clients]
        # convert the datetime string to a datetime object
        datetime_obj = datetime.strptime(values['dateTimeCollectOrder'], '%Y-%m-%dT%H:%M')
        # extract the date part of the datetime object
        date_obj = datetime_obj.date()
        exclude_keys = ['collector', 'csrfmiddlewaretoken', 'dateTimeCollectOrder']

        total = 0
        for key, value in values.items():
            if key not in exclude_keys or key.isdigit():
                print(f"key of the value to be addedd => {key}")
                if value.isdigit():
                    total += int(value)
                else:
                    break

        print("value => ", value)
        client_instances = Client.objects.filter(id__in=clients)
        areas_instance   = Area.objects.filter(id__in=areas) 
        collect_order = CollectOrder.objects.create(
            collector=values['collector'],
            required=total,
            created_prev_date=date_obj
        )
        collect_order.clients.set(client_instances)
        collect_order.areas.set(areas_instance)
        collectOrderId = collect_order.id
        newcollectRecord = CollectRecord.objects.create(
            collectOrder = collect_order,
            serial       = collectRecordSerial,
            receiptNum   = collectRecordreceiptNum
        )
        print('new_record => ', collectOrderId)
        status = {'msg':'done', 'collectOrder': collectOrderId, 'newcollectRecord id ': newcollectRecord.id}
        return Response(status)

class getCollectorsAll(APIView):
    def get(self, request):
        collectorsRcords = Employee.objects.all()
        collectors = [{"id":collector.id, "name": collector.name} for collector in collectorsRcords if collector.job2 == "collector"]
        return Response(collectors)


class CancelContractView(View):
    def get(self, request, client_id):
        client = Client.objects.get(id=client_id)
        client.is_deleted = True
        client.save()
        prev_url = request.META.get('HTTP_REFERER')
        return redirect(prev_url)

# class createCollectOrder(APIView):
#     def post(self, request):
#         data2 = json.loads(request.body)
#         if 'confirm' in data2:
#             # here code to confirm already previous created collect order
#             pass
#         else:
#             # new collct order to be created

#             collectOrder = CollectOrder.objects.create()
#             data={"msg":"done", "collectOrderId":collectOrder.id}
#         return Response(data)

class clientNestedTable(APIView):
    def post(self, request):
        data2 = json.loads(request.body)
        if 'contractId' in data2:
            contractId = data2['contractId']
        else:
            print("erorr here no contract id provided")
        contract = Contract.objects.get(pk=contractId)
        follows = FollowContractServices.objects.filter(client=contract.client)
        if follows.count() > 0:
            dataList = []
            thead = {"contractId":"سريال التعاقد","services":"الخدمات", "month":"الشهر", "statue":"الحالة"}
            for follow in follows:
                print(f"follow =// => {follow}")
                temp = {}
                temp["contractId"]          = contract.id
                temp["services"]            = [serv.name for serv in contract.services.all()]
                temp["month"]               = follow.collected_month
                temp["statue"]              = follow.collcetStatus

                dataList.append(temp)
            data = {"thead":thead, "rows":dataList}
        else:
            data = {}
        return Response(data)

class clientsToPayTable(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        if 'page' in data2:
            page = int(data2['page'])
        else:
            page = 1
        print(f"======== page {page}")
        dataList = []
        basic_start = 0
        basic_end = 20
        start = (page-1)*basic_end
        end = basic_end*page
        if 'name' in data2:
            follows = FollowContractServices.objects.all().filter(is_deleted=False, collcetStatus="pr")
            contractss = [Contract.objects.filter(client=fol.client) for fol in follows]
        elif 'phone' in data2:
            follows = FollowContractServices.objects.filter(is_deleted=False, collcetStatus="pr")
            contractss = [Contract.objects.filter(client=fol.client) for fol in follows]
        else:
            follows = FollowContractServices.objects.all().filter(is_deleted=False, collcetStatus="pr")
            follows = follows.order_by('-pk')
            print(f"follows => {follows}")
            contractss = [Contract.objects.filter(client=fol.client) for fol in follows]
        count = follows.count()
        if count > 0:
            contracts=contractss[start:end]
            thead = {"contractSerial":"سريال التعاقد", "contract_date":"تاريخ التعاقد","clientName":"اسم العميل","phone":"رقم الهاتف","area":"المنطقة",
                    "addresss_details":"العنوان بالتفصيل", "desirved":"المستحق", "notes":"الملاحظات"}
            print(f"contracts => {contracts}")
            for contract in contracts:
                print(f"contract =// => {contract}")
                temp = {}
                temp["contractId"]          = contract[0].id
                temp["contractSerial"]      = contract[0].serialNum
                temp["contract_date"]       = contract[0].created_prev_date
                temp["clientName"]          = contract[0].client.name
                temp["phone"]               = contract[0].client.phone
                temp["addresss_details"]    = contract[0].client.addressDetails
                temp["desirved"]            = contract[0].client.deserved
                temp["notes"]               = contract[0].client.notes
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList,'count':count, 'start':start, 'end':end}
        else:
            data = {}
        return Response(data)

class collectionRequestCancel(APIView):
    def post(self,request):
        data2=json.loads(request.body)
        requestId = data2['requestId']
        collect = CollectOrder.objects.get(pk=requestId)
        collect.is_deleted=True
        collect.save()
        data = {'msg':'done'}
        return Response(data)

class collectionRequestUnConfirm(APIView):
    def post(self,request):
        data2=json.loads(request.body)
        requestId = data2['requestId']
        collect = CollectOrder.objects.get(pk=requestId)
        collect.confirmed=False
        collect.reason = data2['reason']
        collect.save()
        data = {'msg':'done'}
        return Response(data)

class collectionRequestConfirm(APIView):
    def post(self,request):
        data2=json.loads(request.body)
        requestId = data2['requestId']
        collect = CollectOrder.objects.get(pk=requestId)
        collect.confirmed=True
        collect.save()
        data = {'msg':'done'}
        return Response(data)

class collectionRequestsHistory(APIView):
    def get(self, request):
        page =  1
        print(f"======== page {page}")
        dataList = []
        basic_start = 0
        basic_end = 20
        start = (int(page)-1)*basic_end
        end = basic_end*int(page)
        collectRows = CollectOrder.objects.filter(is_deleted=False)
        if collectRows.count() > 0:
            collects=collectRows.order_by('-id')
            thead = {"requestId":"رقم الطلب", "collector":"اسم المحصل","areas":"المنطقة / المناطق",
                    "request_date":"تاريخ الطلب", "statue":"تأكيد التحصيل", "required":"مطلوب تحصيله"}
            for collect in collects:
                temp = {}
                temp["requestId"]      = collect.id
                temp["collector"]      = collect.collector.name
                temp["areas"]          = [area.name for area in collect.areas.all()]
                temp["request_date"]   = collect.created_prev_date
                temp["statue"]         = collect.confirmed
                temp["required"]       = collect.required
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList, 'start':start, 'end':end}
        else:
            data = {}
        return Response(data)
    def post(self, request):
        data2=json.loads(request.body)
        page = data2['page'] if 'page' in data2 else 1
        print(f"======== page {page}")
        dataList = []
        basic_start = 0
        basic_end = 20
        start = (int(page)-1)*basic_end
        end = basic_end*int(page)
        if 'area' in data2:
            area = data2['area']
            collectRows = CollectOrder.objects.filter(Q(areas__name__icontains=area)& Q(is_deleted=False)).distinct()
        elif 'request_date' in data2:
            request_date = data2['request_date']
            collectRows = CollectOrder.objects.filter(Q(created_prev_date=request_date)& Q(is_deleted=False)).distinct()
        elif 'requestId' in data2:
            requestId = data2['requestId']
            collectRows = CollectOrder.objects.filter(Q(pk=requestId)& Q(is_deleted=False)).distinct()
        elif 'requestStatue' in data2:
            requestStatue = data2['requestStatue']
            confirmed = True if requestStatue == "confirmed" else False
            collectRows = CollectOrder.objects.filter(Q(confirmed=confirmed)& Q(is_deleted=False)).distinct()
        else:
            collectRows = CollectOrder.objects.filter(is_deleted=False)
        if collectRows.count() > 0:
            collects=collectRows.order_by('-id')[start:end]
            thead = {"requestId":"رقم الطلب", "collector":"اسم المحصل","areas":"المنطقة / المناطق",
                    "request_date":"تاريخ الطلب", "statue":"تأكيد التحصيل", "required":"مطلوب تحصيله"}
            for collect in collects:
                temp = {}
                temp["requestId"]      = collect.id
                temp["collector"]      = collect.collector.name
                temp["areas"]          = [area.name for area in collect.areas.all()]
                temp["request_date"]   = collect.created_prev_date
                temp["statue"]         = collect.confirmed
                temp["required"]       = collect.required
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList, 'start':start, 'end':end}
        else:
            data = {}
        return Response(data)

class clientProfile(APIView):
    def post(self, request):
        data2              = json.loads(request.body)
        clientId           = data2['id']
        client             = Client.objects.get(pk=clientId)
        name               = client.name
        phoneNumber        = client.phone
        area               = client.area.name
        addressdetails     = client.addressDetails
        contract           = Contract.objects.get(client=client)
        services           = [serv.name for serv in contract.services.all()]
        contractSerial     = contract.serialNum
        contractdate       = contract.created_prev_date
        collectionState    = 'غير محدد'
        requestedPayements = '10000'
        data = {'name':name, 'phoneNumber':phoneNumber, 'area':area,'addressdetails':addressdetails,
        'services':services,'contractSerial':contractSerial, 'contractdate':contractdate,
        'collectionState':collectionState,'requestedPayements':requestedPayements
        }
        return Response(data)

class clientHistory(APIView):
    def post(self, request):
        date = '20-05-2023'
        payement_done = 15
        collector = 'محمد على'
        services = ['جمع منزلى']
        collectionHistory={'date':date,'payement_done':payement_done, 'collector':collector, 'services':services}
        data = {'collectionHistory':collectionHistory}
        return Response(data)

class OngoingCollectionRequests(APIView):
    def get(self, request):
        iscollectOrders = CollectOrder.objects.filter(confirmed=False,is_deleted=False).count()
        if iscollectOrders > 0:
            collect_list2 = []
            for collect in CollectOrder.objects.filter(confirmed=False,is_deleted=False):
                requestId = collect.id
                areas     = [area.name for area in collect.areas.all()]
                collector  = Employee.objects.get(pk=collect.collector.id).name
                temp_dict = {'requestId':requestId, 'areas':areas, 'collector':collector}
                collect_list2.append(temp_dict)
                print(collect_list2)
            data = collect_list2
        else:
        # data = {'collector':collector, 'areas':areas, 'requestId':requestId}
            data = {[]}
        return Response(data)

class currentCollectionRequest(APIView):
    def get(self, request):
        dataList = []
        page = 1
        basic_start = 0
        basic_end = 20
        start = (page-1)*basic_end
        end = basic_end*page
        count = CollectOrder.objects.all().count()
        if count > 0:
            contracts=CollectOrder.objects.all().order_by('-id')[start:end]
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
                temp["billSerial"]     = "004592"
                dataList.append(temp)
            data = {"thead":thead, "rows":dataList, 'start':start, 'end':end}
        return Response(data)

@api_view(('GET',))
def getsubServicesAll(request):
    serviceId = request.GET.get('mainService')
    service = Service.objects.get(pk=serviceId)
    subservices = []
    for serv in SubService.objects.filter(baseService=service):
        temp = {"serviceName":"","serviceId":""}
        temp.update({"serviceName":serv.name,"serviceId":serv.id})
        subservices.append(temp)
    data = {'subServcices':subservices}
    return Response(data)


def TnewCollectOrder(request):
    if 'group' not in request.session:
        return redirect('/cAccounts/login/')
    
    if request.session['group'] == "tahsealAdmin":
        pass
    
    elif request.session['group'] == "dataEntryAdmin":
        pass
    else:
        return HttpResponse("erorr here")
    collectManager()
    areas = Area.objects.all()
    isContracts = True
    contract_list = []
    
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        search_areas = request.POST.getlist('areas[]')
        print(f"search_query => {search_query}")
        if len(search_query) < 2:
            follows = FollowContractServices.objects.filter(
                Q(collcetStatus="pr"),
                Q(),
                Q(client__name__icontains=search_query)       |
                Q(client__phone__icontains=search_query)      |
                Q(client__area__name__icontains=search_query) |
                Q(client__serialNum__icontains=search_query) 
            ).order_by('-created_at')
        elif len(search_areas) >= 0:
            follows = FollowContractServices.objects.filter(
                Q(collcetStatus="pr"),
                Q(client__area__in=search_areas)   ,
            ).order_by('-created_at')
        else:
            follows = FollowContractServices.objects.filter(collcetStatus="pw").order_by('-created_at')
        
        for follow in follows:
            contract = Contract.objects.get(client=follow.client)
            contract_deserved = follow.remainAmount
            clientId = contract.client.id
            Client.objects.filter(pk=clientId).update(deserved=contract_deserved)
            if contract not in contract_list:
                contract_list.append(contract)
        count = len(contract_list)
    else:
        follows = FollowContractServices.objects.filter(collcetStatus="pr", is_deleted=False).order_by('-created_at')
        for follow in follows:
            contract = Contract.objects.get(client=follow.client)
            if contract not in contract_list:
                contract_list.append(contract)
        count = len(contract_list)
        
    if count == 0:
        isContracts = False
        
    ctx = {'areas':areas, 'contracts':contract_list, 'clientsCount':count, 'isContracts':isContracts}
    return render(request,'DataEntry/TnewCollectOrder.html',ctx)

class currentContractTableSearchFilter(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        dateQuery   = data2['create_date']  if 'create_date' in data2 else ''
        statueQuery = data2['statue']       if 'statue' in data2 else ''
        query  = data2['other']   # serialNumber - name - area - notes - serviceName - created by
        if dateQuery:
            filteredContracts = Contract.objects.filter(created_prev_date=dateQuery,is_deleted=False).distinct()
        elif statueQuery:
            filteredContracts = []
        elif query:
            filteredContracts = Contract.objects.filter(
            Q(client__serialNum__icontains=query)& Q(is_deleted=False) |
            Q(client__name__icontains=query)& Q(is_deleted=False) |  Q(client__area__name__icontains=query)& Q(is_deleted=False)|
            Q(belong_to__name__icontains=query)& Q(is_deleted=False) |Q(notes__icontains=query)& Q(is_deleted=False) |
            Q(created_by__name__icontains=query)& Q(is_deleted=False)|Q(services__name__icontains=query)& Q(is_deleted=False)
        ).distinct()
        else:
            filteredContracts = Contract.objects.all()
        data = getCurrentContractTable(data2, filteredContracts)
        return Response(data)

class deleteContract(APIView):
    def post(self,request):
        data2=json.loads(request.body)
        contractId = data2["contractId"]
        # Contract.objects.filter(pk=contractId, is_deleted=False).update(is_deleted=True)
        contract = Contract.objects.get(pk=contractId)
        print(f"contractId => {contractId}")
        client = contract.client
        clientId = client.id
        Client.objects.filter(pk=clientId, is_deleted=False).update(is_deleted=True)
        data = {'msg': 'done'}
        return Response(data)

@api_view(['POST'])
def ConfirmContract(request):
    print('testing')
    ## get param val from url
    # contractId = request.POST.get('contractId')
    data2=json.loads(request.body)
    contractId = data2["contractId"]
    # Contract.objects.filter(pk=contractId).update(is_test=False)
    contract = Contract.objects.get(pk=contractId)
    client = contract.client
    clientId = client.id
    Client.objects.filter(pk=clientId, is_deleted=False).update(missing_info=False)
    print(f"contractId => {contractId}  / /  clientId => {clientId}")
    Client.objects.filter(pk=clientId, is_deleted=False).update(is_test=False, missing_info=False)

    newContractId = create_new_contract(data2, clientId)
    # follow Services
    make_new_contract_service_followers(data2, newContractId, clientId)
    data = {'msg': 'done'}
    return Response(data)


# @api_view(('GET',))
# # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def ConfirmContract(request):
#     contractId = request.GET.get('contractId')
#     Contract.objects.filter(pk=contractId).update(is_test=False)
#     contract = Contract.objects.get(serialNum=contractId)
#     client = contract.client
#     clientId = client.id
#     Client.objects.filter(serialNum=contractId).update(is_test=False, missing_info=False)
#     data = {'clientId':clientId,'contract':contractId}
#     data = {'msg': 'done','data':data}
#     return Response(data)

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def TgetcollcetStatus(request):
    contractId = request.GET.get('contractId')
    # clientId = Contract.objects.get(pk=contractId, is_deleted=False, is_test=False).client.id
    clientId = Contract.objects.get(pk=contractId, is_deleted=False).client.id
    client = Client.objects.get(pk=clientId)
    follows = FollowContractServices.objects.filter(client=client)
    followsStatus = ''
    for follow in follows:
        # print(f"follow.collcetStatus => {follow.collcetStatus}")
        if follow.collcetStatus == "pd":
            followsStatus = "تم الدفع"
        elif follow.collcetStatus == "pr":
            followsStatus = "مطلوب الدفع"
        elif follow.collcetStatus == "wecd":
            followsStatus = "فى انتظار ميعاد التحصيل"
    data = {'followsStatus':followsStatus}
    return Response(data)

@login_required
def TCurrentContract(request):
    listcount = 15
    # contracts_list = Contract.objects.filter(is_deleted=False, is_test=False)
    contracts_list = Contract.objects.filter(is_deleted=False)
    query       = request.GET.get('q')
    queryDate   = request.GET.get('qd')
    queryStatue = request.GET.get('qs')
    if query:
        contracts_list = Contract.objects.filter(
            Q(client__serialNum__icontains=query)& Q(is_deleted=False) |
            Q(client__name__icontains=query)& Q(is_deleted=False) |  Q(client__area__name__icontains=query)& Q(is_deleted=False)|
            Q(belong_to__name__icontains=query)& Q(is_deleted=False) |Q(client__customFilter__icontains=query)& Q(is_deleted=False)|
            Q(notes__icontains=query)& Q(is_deleted=False) |Q(created_by__name__icontains=query)& Q(is_deleted=False)|
            Q(services__name__icontains=query)& Q(is_deleted=False)
        ).distinct()
    if queryDate:
        contracts_list = Contract.objects.filter(created_prev_date=queryDate,is_deleted=False).distinct()

    paginator = Paginator(contracts_list, listcount) # 6 posts per page
    page = request.GET.get('page')
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)

    ctx = {'contracts_list':contracts_list, 'contracts':contracts}
    return render(request, 'DataEntry/TCurrentContract.html', ctx)

@api_view(['GET'])
def getServicesOfClient(request):
    clientId   = request.GET.get('clientId')
    clientRecord = Client.objects.get(pk=clientId)
    servicesList = Contract.objects.filter(client=clientRecord)
    if servicesList.count() > 0:
        servicesList = servicesList[0].services
        servicesList = [serv.name  for serv in servicesList.all()]
        services = str(servicesList)
        services2 = " - ".join(servicesList)
    else :
        services = " - "
        services2 = " - "
    data = {'services':services, 'services2':services2}
    return Response(data)

@api_view(['GET'])
def checkClientSerial(request):
    print("test")
    a = "3514351"
    frontSerial   = request.GET.get('serial')
    res = False
    frontSerialExist = Client.objects.filter(serialNum=frontSerial).count()
    print(frontSerialExist)
    if frontSerialExist > 0:
        res = "found"

        a = Client.objects.filter(serialNum=frontSerial)
        a = a[0].name
    else:
        res = "not found"
    data = {'responseText':res, 'itesms':a}
    return Response(data)

@login_required
def TnewContract2(request):
    if 'group' not in request.session :
        return redirect('/cAccounts/login/')
    else :
        pass
    if request.session['group'] == "dataEntryAdmin":
        pass
    elif request.session['group'] == "tahsealAdmin":
        return redirect('/DataEntry/TnewCollectOrder')
    else:
        return HttpResponse("erorr here")
    isServiceManagerAdmin = False
    print(f"request.GET.get('userRole') => {request.GET.get('userRole')}")
    if request.GET.get('userRole'):
        isServiceManagerAdmin = True
    services  = Service.objects.all()
    servicesList = ["service-"+str(service.id) for service in services]
    isClient       = False
    if request.method == 'POST':
        print("here => 4")
        date            = request.POST['date']    # todayUser
        clientId        = request.POST['clientId']
        Client.objects.filter(pk=clientId, is_deleted=False).update(missing_info=False)
        Client.objects.filter(pk=clientId, is_deleted=False).update(notes='')
        userId          = request.POST['userId']
        serial          = request.POST['serial']
        clientName      = request.POST['name']
        phone           = request.POST['phone']
        contractDate    = request.POST['contractDate']
        lastPay = request.POST['lastPay'] if 'lastPay' in request.POST else ''
        area            = Area.objects.get(pk=request.POST['area'])
        addressDetails  = request.POST['addressDetails']
        apartment       = isEmptyStr(request.POST['apartment'])
        flat            = isEmptyStr(request.POST['float'])
        servicesIdsList = request.POST['servicesId']
        servicesIdsList = servicesIdsList.split(',')
        print(f"servicesIdsList => {servicesIdsList}")
        if len(servicesIdsList) <= 1 :
            servicesIdsList = []
            services = request.POST.getlist('service[]')
            for serv in services:
                print(f"services => {serv}")
                servicesPrices = request.POST.getlist('servicePrice[]')
                indexx  = services.index(serv)
                servicePrice = servicesPrices[indexx]
                servicePriceTypes = request.POST.getlist('servicePriceType[]')
                servicePriceType = servicePriceTypes[indexx]
                isServiceExist = checkServiceExist(serv,servicePrice, servicePriceType)
                servcesNotes = request.POST.getlist('notes[]')
                serviceNote  = servcesNotes[indexx]
                servcesNotes = " - ".join(servcesNotes)
                print(f"serviceNote => {serviceNote}  => {servcesNotes}")
                print(f"checkServiceExist => {isServiceExist}")
                if isServiceExist :
                    serviceId = getServiceId(serv, servicePrice ,servicePriceType)
                    servicesIdsList.append(serviceId)
                
                else:
                    serviceTypes = request.POST.getlist('serviceType[]')
                    serviceType  = serviceTypes[indexx]
                    print(f"servicePrice=> {servicePrice}")
                    newServiceId = Service.objects.create(name=serv, typee=serviceType, price=servicePrice,
                                                           priceType=servicePriceType)
                    servicesIdsList.append(newServiceId.id)
        else:
            pass
        # servicesIdsList = servicesIdsList.split(',')
        print(f"servicesIdsList => {servicesIdsList}")
        servicesIdsListint = [int(s) for s in servicesIdsList]
        print(f"request.POST['referer'] => {request.POST['referer']}")
        referer         = 0 if request.POST['referer'] == '0' else request.POST['referer']
        clientServicesList = [Service.objects.get(pk=service) for service in servicesIdsListint ]
        belong_to      = Employee.objects.get(pk=referer) if referer != 0 else 3
        ##########

        # to be done
        if clientId != "" or clientId != None :
            client = Client.objects.get(pk=clientId)
            print(f"client => {client}")
            previous_notes = client.notes
        else:
            previous_notes = ''
        data2 = {
            "name": clientName,
            "clientId": clientId,
            "phone": phone,
            "nationalId": "",
            "Serial": serial,
            "area": area,
            "streetName": addressDetails,
            "addressBuilding": apartment,
            "addressApartment": flat,
            "addressDetails": f"{addressDetails} - {apartment} - {flat}",
            "services": servicesIdsListint,
            "referer": referer,
            "date": date,
            "userId": userId,
            "contractDate":contractDate,
            "lastPay":lastPay,
            "notes": f"{servcesNotes}"
        }


        newClientId  =  create_new_client(data2) # wikk be returened after inserting the new client
        # client contract data
        newContractId = create_new_contract(data2, newClientId)
        # follow Services
        make_new_contract_service_followers(data2, newContractId, newClientId)
        return redirect('/DataEntry/TnewContract/')
    else:
        print("isServiceManagerAdmin =>" , isServiceManagerAdmin)
        # print(f"isClient => {isClient}")
        if request.GET.get('clientId'):
            isClient       = True
            clientId       = request.GET.get('clientId')
            Client.objects.filter(pk=clientId, is_deleted=False).update(missing_info=False)
            Client.objects.filter(pk=clientId, is_deleted=False).update(notes='')
            clientRecord   = Client.objects.get(pk=clientId)
            isContract     = Contract.objects.filter(client=clientRecord)
            clientContract = isContract[0] if isContract.count()>0 else False
            servicesList   = [serv.name for serv in clientContract.services.all()] if isContract.count()>0 else []
            areas     = Area.objects.all()
            employees = Employee.objects.all()
            ctx={'services':services, 'employees':employees, 'areas':areas,'today':todayDate,
            'todayUser':todayUser, 'clientRecord':clientRecord,'clientId':clientId,
            'clientContract':clientContract,'servicesList':servicesList,'isClient':isClient, 'isServiceManagerAdmin':isServiceManagerAdmin}
            return render(request, 'DataEntry/TnewContract.html', ctx)
    areas     = Area.objects.all()
    employees = Employee.objects.all()

    ctx={'services':services, 'employees':employees, 'areas':areas,'today':todayDate,
    'todayUser':todayUser, 'isClient':isClient, 'isServiceManagerAdmin':isServiceManagerAdmin}
    return render(request, 'DataEntry/TnewContract2.html', ctx)

def TnewContract(request):
    if 'group' not in request.session :
        return redirect('/cAccounts/login/')
    else :
        pass
    if request.session['group'] == "dataEntryAdmin":
        pass
    elif request.session['group'] == "tahsealAdmin":
        return redirect('/DataEntry/TnewCollectOrder')
    else:
        return HttpResponse("erorr here")
    services  = Service.objects.all()
    servicesList = ["service-"+str(service.id) for service in services]
    temp = True
    continueContractsRecords = Client.objects.filter(missing_info=True, is_deleted=False)
    isClient       = False
    if request.method == 'POST':
        print("here => 2")
        date            = request.POST['date']    # todayUser
        clientId        = request.POST['clientId']
        if clientId == 0:
            Client.objects.filter(pk=clientId, is_deleted=False).update(missing_info=False, is_deleted=False)
            Client.objects.filter(pk=clientId, is_deleted=False).update(notes='', is_deleted=False)
        else:
            pass
        userId          = request.POST['userId']
        serial          = request.POST['serial']
        clientName      = request.POST['name']
        phone           = request.POST['phone']
        contractDate    = request.POST['contractDate']
        lastPay = request.POST['lastPay'] if 'lastPay' in request.POST else ''
        area            = Area.objects.get(pk=request.POST['area'])
        addressDetails  = request.POST['addressDetails']
        apartment       = isEmptyStr(request.POST['apartment'])
        flat            = isEmptyStr(request.POST['float'])
        servicesIdsList = request.POST['servicesId']
        print("here => 1")
        print(f"len servicesIdsList => {len(servicesIdsList)}")
        if len(servicesIdsList) <= 1 :
            servicesIdsList = []
            services = request.POST.getlist('service[]')
            for serv in services:
                print(f"services => {serv}")
                servicesPrices = request.POST.getlist('servicePrice[]')
                indexx  = services.index(serv)
                servicePrice = servicesPrices[indexx]
                servicePriceTypes = request.POST.getlist('servicePriceType[]')
                servicePriceType = servicePriceTypes[indexx]
                isServiceExist = checkServiceExist(serv,servicePrice, servicePriceType)
                servcesNotes = request.POST.getlist('notes[]')
                servcesNotes = " - ".join(servcesNotes)
                serviceNote  = servcesNotes[indexx]
                print(f"serviceNote => {serviceNote}  => {servcesNotes}")
                print(f"checkServiceExist => {isServiceExist}")
                if isServiceExist :
                    serviceId = getServiceId(serv, servicePrice ,servicePriceType)
                    servicesIdsList.append(serviceId)
                else:
                    serviceTypes = request.POST.getlist('serviceType[]')
                    serviceType  = serviceTypes[indexx]
                    print(f"servicePrice=> {servicePrice}")
                    newServiceId = Service.objects.create(name=serv, typee=serviceType, price=servicePrice)
                    servicesIdsList.append(newServiceId.id)
        else:
            pass
        # servicesIdsList = servicesIdsList.split(',')
        print(f"servicesIdsList => {servicesIdsList}")
        servicesIdsListint = [int(s) for s in servicesIdsList]
        referer         = 0 if request.POST['referer'] == '0' else request.POST['referer']
        clientServicesList = [Service.objects.get(pk=service) for service in servicesIdsListint ]
        belong_to      = Employee.objects.get(pk=referer) if referer != 0 else ''
        ##########

        # to be done
        if clientId != "" or clientId != None :
            previous_notes = clientId.notes
        else:
            previous_notes = ''
        data2 = {
            "name": clientName,
            "clientId": clientId,
            "phone": phone,
            "nationalId": "",
            "Serial": serial,
            "area": area,
            "streetName": addressDetails,
            "addressBuilding": apartment,
            "addressApartment": flat,
            "addressDetails": f"{addressDetails} - {apartment} - {flat}",
            "services": servicesIdsListint,
            "referer": referer,
            "date": date,
            "userId": userId,
            "contractDate":contractDate,
            "notes": f"{servcesNotes}"
        }


        newClientId  =  create_new_client(data2) # wikk be returened after inserting the new client
        # client contract data
        newContractId = create_new_contract(data2, newClientId)
        # follow Services
        make_new_contract_service_followers(data2, newContractId, newClientId)
        return redirect('/DataEntry/')
    else:
        if request.GET.get('clientId'):
            isClient       = True
            clientId       = request.GET.get('clientId')
            clientRecord   = Client.objects.get(pk=clientId)
            isContract     = Contract.objects.filter(client=clientRecord)
            clientContract = isContract[0] if isContract.count()>0 else False
            servicesList   = [serv.name for serv in clientContract.services.all()] if isContract.count()>0 else []
            areas     = Area.objects.all()
            employees = Employee.objects.all()
            ctx={'services':services, 'employees':employees, 'areas':areas,'today':todayDate,
            'todayUser':todayUser, 'contracts':continueContractsRecords, 'clientRecord':clientRecord,
            'clientContract':clientContract,'servicesList':servicesList,'isClient':isClient}
            return render(request, 'DataEntry/TnewContract.html', ctx)
    areas     = Area.objects.all()
    employees = Employee.objects.all()
    ctx={'services':services, 'employees':employees, 'areas':areas,'today':todayDate,
    'todayUser':todayUser, 'contracts':continueContractsRecords, 'isClient':isClient}
    return render(request, 'DataEntry/TnewContract.html', ctx)

import math
def getPageNums(total, listcount):
    pages = math.ceil(total/listcount)
    return pages

@login_required
def TmainPage(request):
    print(f"request.session['group'] => {request.session.keys()}")
    if 'group' not in request.session :
        return redirect('/cAccounts/login/')
    else :
        pass
    if request.session['group'] == "dataEntryAdmin":
        pass
    elif request.session['group'] == "tahsealAdmin":
        pass
    else:
        return HttpResponse("erorr here")
    listcount = 7
    # stats part
    remainingCollections = len(peopleTocollectFrom())
    collected            = len(peopleCollectedFrom())
    currentClients       = Contract.objects.all().count()
    collectorsNum        = Employee.objects.filter(jobTitle="موظف تحصيل").count()
    # latest contracts
    contracts            = Contract.objects.all().order_by('-id')

    pages = getPageNums(Contract.objects.all().count(), listcount)
    # current collecr orders
    orders               = CollectOrder.objects.filter(confirmed=False)
    ctx= {'remainingCollections':remainingCollections, "collected":collected, "currentClients":currentClients, "collectorsNum":collectorsNum,
        'items':contracts, 'contractsLen':contracts.count(), 'orders':orders, 'ordersLen':orders.count(),
        'pages':pages, 'listcount':listcount}

    # check if clients has a service id in the client record 
    # make a contract with this service to the client 
    # make a follow service for the client with it's contract and service

    autoServiceAdd()
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
        clients = data2['clients']
        clients = clients.split(',')

        areas = data2["areas"]
        areas = areas.split(',')
        clients_set = manyToManyIdSave(clients, Client)
        areas_set = manyToManyIdSave(areas, Area)
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
        follows = FollowContractServices.objects.filter(collcetStatus="pw")
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
        data2=json.loads(request.body)
        page = data2['page']
        print(f"======== page {page}")
        dataList = []
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
    def get(self, request):
        dataList = []
        page = 1
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
                temp["requestId"] = order.id
                temp["collector"] = order.collector.name
                temp["clientsNum"]= order.clients.count()
                temp["areas"]     = [area.name for area in order.areas.all()]
                temp["date"]      = order.created_at_date
                dataList.append(temp)
            data = dataList
        else:
            data = {}
        return Response(data)

class recentContracts(APIView):
    def get(self,request):
        contracts            = Contract.objects.all().order_by('-id')[:20]
        data = generateTable(contracts, "recentContracts")
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
        # for obj in Client.objects.all():
        #     obj.notes=''
        #     obj.save()
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
# check if clients has a service id in the client record 
    # make a contract with this service to the client 
    # make a follow service for the client with it's contract and service

def autoServiceAdd():
    print(f"autoServiceAdd => started")
    status = {'msg':'-'}
    clients = Client.objects.filter(is_deleted=False)
    for client in clients :
        clientId = client.id
        if client.serviceId != None:
            # print(f"client has serviceId id => {clientId}")
            serviceId = client.serviceId
            date_obj = client.created_prev_date
            date_str = date_obj.strftime('%Y-%m-%d')
            #data2
            data2 = {"Serial":client.serialNum, "referer":"3",
                     "date": date_str, "userId": "1",
                     "services":f"{serviceId}"
                     }   # 1 => data entry    shimaa

            newContractId = create_new_contract(data2, clientId)
            # follow Services
            make_new_contract_service_followers(data2, newContractId, clientId)
        else:
            pass
            # print(f"client hasnot serviceId id => {clientId}")

def correctCollectMonth():
    follows = FollowContractServices.objects.filter(is_deleted=False)
    for follow in follows :
        
        if follow.collectedDate == None:
            contractDate = Contract.objects.filter(client=follow.client, is_deleted=False)[0].created_prev_date
            lastPayDate = contractDate
        else:
            lastPayDate = follow.collectedDate
        thirtyDaysAfter = lastPayDate+ timezone.timedelta(days=30)
        current = timezone.now()
        current_date = current.date()
        # print(f"type of thirtyDaysAfter is {type(thirtyDaysAfter)}")
        if thirtyDaysAfter < current_date:
            print(f"thirtyDaysAfter > lastPayDate {thirtyDaysAfter} => {lastPayDate} YES")
            if follow.collcetStatus == "pip":
                follow.collectedDate = current_date
            else:
                follow.collcetStatus="pr"
            print(f"follow client {follow.client.name} / serialNum => {follow.client.serialNum}  thirtyDaysAfter.month => {thirtyDaysAfter.month}")
            follow.ecd          = thirtyDaysAfter
            
            follow.collectMonth = thirtyDaysAfter.month
            follow.year         = thirtyDaysAfter.year
            follow.save()
        else:
            # print(f"thirtyDaysAfter > lastPayDate {thirtyDaysAfter} => {lastPayDate} NO")
            follow.collcetStatus="wecd"
            follow.save()

def collectManager():
    # temprory use now only
    # print(f" # temprory use now only")
    # correctCollectMonth()

    statue = {'msg':'start'}   # for debugging
    updatedCount = 0
    follows = FollowContractServices.objects.filter(is_deleted=False)
    for follow in follows :
        # print(f"follow id => {follow.id}")
        ecd_ecd = follow.ecd
        contract = Contract.objects.filter(client=follow.client).update(ecd=ecd_ecd)
        contract = Contract.objects.filter(client=follow.client).update(remainAmount=follow.remainAmount)
        contract = Contract.objects.get(client=follow.client)
        # FollowContractServices.objects.filter(pk=follow.id).update(area=follow.client.area.name)
        Client.objects.filter(pk=contract.client.id).update(deserved=follow.remainAmount)
        # print("client id => {contract.client.id} follow")

        if follow.collectedDate == None:
            contractDate = Contract.objects.filter(client=follow.client, is_deleted=False)[0].created_prev_date
            lastPayDate = contractDate
        else:
            lastPayDate = follow.collectedDate
        thirtyDaysAfter = lastPayDate+ timezone.timedelta(days=30)
        current = timezone.now()
        current_date = current.date()
        # print(f"type of thirtyDaysAfter is {type(thirtyDaysAfter)}")

        if thirtyDaysAfter < current_date:
            # print(f"thirtyDaysAfter > lastPayDate {thirtyDaysAfter} => {lastPayDate} YES")
            if follow.collcetStatus == "pip":
                follow.collectedDate = current_date
            else:
                follow.collcetStatus="pr"
            follow.save()
        else:
            # print(f"thirtyDaysAfter > lastPayDate {thirtyDaysAfter} => {lastPayDate} NO")
            follow.collcetStatus="wecd"
            follow.save()
    follows = FollowContractServices.objects.filter(collcetStatus="wecd", is_deleted=False)
    followsCount = follows.count()
    statue['count'] = followsCount
    clients = Client.objects.filter(is_deleted=False)
    for client in clients:
        clientFollows = FollowContractServices.objects.filter(
                client=client,
                collcetStatus="مطلوب الدفع",
                service__priceType="month",
                is_deleted=False
            ).values('client').annotate(total_pay=Sum('deservedAmount'))
        
        client.deserved = clientFollows[0]['total_pay'] if clientFollows else 0
        client.save()
        statue['updatedCount'] = updatedCount
    return statue
# def collectManager():
#     statue = {'msg':'start'}   # for debugging
#     ####  how to it
#     ##  i want to get all follows that has the 
#     ## 
#     ##  
#     ## 
#     tahselaStart = 25
#     tahsealEnd = 5
#     today = datetime.now()
#     todaynum = today.day
#     currentMonth = today.month
#     if tahselaStart <= todaynum <= tahsealEnd:
#         follows = FollowContractServices.objects.filter(collected_month=currentMonth,  collcetStatusNums="فى انتظار ميعاد التحصيل", is_deleted=False)
#         followsCount = follows.count()
#         statue['count'] = followsCount
#         # need to calculate payment of all clients and add everyone payement to it's desireved
#         updatedCount = follows.update(collcetStatusNums="مطلوب الدفع", is_deleted=False)
#         clients = Client.objects.filter(is_deleted=False)
#         for client in clients:
#             clientFollows = FollowContractServices.objects.filter(
#                     client=client,
#                     collcetStatusNums="مطلوب الدفع",
#                     service__priceType="month",
#                     is_deleted=False
#                 ).values('client').annotate(total_pay=Sum('deservedAmount'))
            
#             client.deserved = clientFollows[0]['total_pay'] if clientFollows else 0
#             client.save()
            
#             # print(f"client {client.id} client total deserved => {client.deserved}")


#         statue['updatedCount'] = updatedCount
#     else:
        
#         statue.msg = 'today not any of tahseal days'

#     return statue

def getServiceId(service, servicePrice, servicePriceType) :
    serviceExist = Service.objects.get(name=service, price=servicePrice, priceType=servicePriceType)
    return serviceExist.id

def checkServiceExist(service, servicePrice, servicePriceType):
    serviceExist = Service.objects.filter(name=service, price=servicePrice, priceType=servicePriceType).count()
    print(f"serviceExist => {serviceExist}")
    if serviceExist > 0 :
        serviceExist = True
    else:
        serviceExist = False
    return serviceExist

def getCurrentContractTable(data2, filteredContracts):
    if 'page' in data2:
        page = data2['page']
    else:
        page = 0
    print(f"======== page {page}")
    dataList = []
    basic_start = 0
    basic_end = 20
    start = (page-1)*basic_end
    end = basic_end*page
    count = filteredContracts.count()
    if count > 0:
        contracts=filteredContracts.order_by('-id')[start:end]
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
    return data

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

    if tableType == "recentContracts":
        thead = {"contractSerial":"سريال الفاتورة","contractDate":"تاريخ التعاقد",
                "clientName":"اسم العميل","phone":"رقم الهاتف","area":"المنطقة",
                "addressDetails":"العنوان بالتفصيل",
                "services":"الخدمات",
                "deserved":"المستحق", "notes":"الملاحظات"}
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
                servicesList           = [serv.name for serv in contracts.services.all() ]
                temp["services"]       = ' - '.join(servicesList)
                temp["deserved"]  = contracts.client.deserved
                temp["notes"]     = contracts.client.notes
                dataList.append(temp)
        table = {"thead":thead, "rows":dataList}
    return table

def set_follow_areas_name(follows):
    for follow in follows:
        FollowContractServices.objects.filter(pk=follow.id).update(area=follow.client.area.name)

# erorr
# set_follow_areas_name(FollowContractServices.objects.all())

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
    print(f"manyToManyList => {manyToManyList}")
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
    clientId                =   contract.client.id
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
            service=service_self, startingDate=contractDate,deservedAmount=service_self.price, remainAmount=service_self.price,
            collectMonth=get_month(data2['date']),created_by=Employee.objects.get(pk=data2['userId'])
        )
        contract_deserved = follow_contract_services.remainAmount
        Client.objects.filter(pk=clientId).update(deserved=contract_deserved)
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
        if follow.collcetStatus == "مطلوب الدفع":
            status = "مطلوب الدفع"
    return status

def checkToChangecollectStatue(follos):
    # with fixed time  25
    pass
    # with passing the typee of the service

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
    if cl.area=="-" or cl.name=="-" or cl.serialNum=="-" or cl.phone == "-" or cl.area == None or cl.name == None or cl.serialNum == None or cl.phone == None or cl.area == "" or cl.serialNum=="" or cl.name == "" or cl.phone == "":
        cond = True
    else:
        cond = False
    return cond

def clientRequest(client):
    cond = False
    return cond

def peopleCollectedFrom():
    names_list = []
    follows = FollowContractServices.objects.filter(collcetStatus="pd")
    # print(f"follows => {follows}")
    for follow in follows:
        client = follow.client
        is_count = FollowContractServices.objects.filter(client=client,collcetStatus="pr").count()
        if is_count == 0:
            names_list.append(follow.client.name)
        else:
            pass
    client_names =  sorted(set(names_list))
    return client_names

def peopleTocollectFrom():
    names_list = []
    follows = FollowContractServices.objects.filter(collcetStatus='pr')
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
                month = date_formatted.month
            else:
                month = 1
        else:
            month = date_formatted.month
        # print(f"this month is {month}")
        return month

    client                  =   Client.objects.get(pk=newClientId)
    contract                =   Contract.objects.get(pk=newContractId)
    service_objects_list    =   data2["services"]
    for service in service_objects_list:
        service_self = Service.objects.get(pk=service)
        follow_contract_services = FollowContractServices.objects.update_or_create(
            client=client,service=service_self,
            defaults={
                'client':client, 'service':service_self, 'deservedAmount':service_self.price, 'remainAmount':service_self.price,
                'collectMonth':get_month(data2['date']),'created_by':Employee.objects.get(pk=data2['userId']), 'is_test':False
            }
        )


def create_new_contract(data, newClientId):
    services_list = data["services"]
    services_id_list = []
    services_set = set()
    i = 0
    for service in services_list:
        serv = Service.objects.get(pk=service)
        services_set.add(serv)
        i += 1
    last_pay_value = data.get('lastPay', None)  # Get lastPay value from data if it exists, else use None
    contract = Contract.objects.update_or_create(
        client=Client.objects.get(pk=newClientId),
        defaults={
            'serialNum':data["Serial"],'client':Client.objects.get(pk=newClientId),
            'belong_to':Employee.objects.get(pk=data['referer'] if data['referer'] != 0 else 3),
            'created_prev_date':data['date'],'lastPay':last_pay_value,
            'created_by':Employee.objects.get(pk=data['userId']), 'is_test':False
        }
    )
    contract = Contract.objects.get(client=Client.objects.get(pk=newClientId))
    contract.services.set(services_set)
    contract.save()
    contract_id = contract.id
    return contract_id

def update_client_data(dictt):
    # Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
    clientId = dictt["id"]
    client = Client.objects.filter(pk=clientId, is_deleted=False)
    client.update(
        name=dictt["name"],phone=dictt["phone"],nationalId=dictt["nationalId"], password="",
        serialNum=dictt["Serial"],area=Area.objects.filter(name=dictt["area"])[0],streetName=dictt["streetName"],addressBuilding=dictt["addressBuilding"],
        addressApartment=dictt["addressApartment"],addressDetails=dictt["addressDetails"],created_prev_date=dictt["date"],
        created_by=Employee.objects.get(pk=dictt['userId'], is_test=False)
        )
    return clientId

def create_new_client(dictt):
    # print(f'dictt["clientId"] => {dictt["clientId"]}')
    client, created = Client.objects.update_or_create(
        serialNum=dictt["Serial"],name=dictt["name"],
        defaults = {
            'serialNum':dictt["Serial"],'name':dictt["name"],'phone':dictt["phone"],'nationalId':dictt["nationalId"], 'password':"",
            'area':Area.objects.filter(name=dictt["area"])[0],'streetName':dictt["streetName"],
            'addressBuilding':dictt["addressBuilding"],'addressApartment':dictt["addressApartment"],'addressDetails':dictt["addressDetails"],
            'created_prev_date':dictt["date"], 'notes':dictt["notes"] ,
            'contractDate':dictt["contractDate"],'created_by':Employee.objects.get(pk=dictt['userId'])
        }
    )
    client_id = client.id
    return client_id


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

        if cl.area or  cl.name or cl.phone == "-" or cl.area or cl.name or cl.phone is None or cl.area or cl.name  or cl.phone == "":
            temp += 1
            cl.missing_info = True
            if cl.area == "-" or cl.area is None or cl.area == "":
                notes += "المنطقة غير محددة\n"
            if cl.name == "-" or cl.name is None or cl.name == "":
                notes += "الإسم غير كامل أو غير مكتوب\n"
            if cl.serialNum == "-" or cl.serialNum is None or cl.serialNum == "":
                notes += "خطأ برقم السريال\n"
            if cl.phone == "-" or cl.name is None or cl.name == "" or len(str(cl.phone)) > 11 or len(str(cl.phone)) < 10:
                notes += "خطأ برقم التليفون \n"
            print(f'client id --> {cl.id} is missing area')
            cl.notes = notes
            print(f"client notes ==> {notes}")
            cl.save()
        else:
            cl.missing_info=False
            cl.save
    print(f"total {temp} clients // done all clients check")