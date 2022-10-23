from lib2to3.pgen2 import token
from urllib import request, response
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import APIException, AuthenticationFailed

from DataEntry.models import *
from django.core import serializers as core_serializers
from DataEntry.serializers import ContractSerializer, ServiceSerializer, ClientSerializer
from django.core.exceptions import ObjectDoesNotExist
from .authentication import *

class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data= {'message':'success'}
        return response

class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({'token': access_token})

class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = Client.objects.filter(pk=id).first()
            return Response(ClientSerializer(user).data)
        raise AuthenticationFailed("unauthenticated")

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the account index.")
def collectionDay(request):
    collection_day = "test"
    return HttpResponse(collection_day)




def clientDataForMobile(clientId, key, access_token):
    if key == "login":
        msg = "تم تسجيل الدخول بنجاح"
    else:
        msg = "تم التسجيل بنجاح"

    user = Client.objects.get(id=clientId)
    client_name = str(user.name)
    # data = {"temp", str(client_name)}
    data = {"responseStatusId":"1", "isRequested":"2" if user.activation_request == True  else "1","message" : msg, "clientId":str(user.id),"name":str(client_name) , "phone":user.phone , "nationalId":user.nationalId , "area":"مدينة ناصر" ,"streetName":user.streetName  ,"buildingNumber":user.addressBuilding, "apartementNumber":user.addressApartment, "token":access_token}
    return data

def validateFirstRegisterData(name,nationalId,phone,password):
    data_good     = True
    erorr_message = ""
    data          = {}
    # tobe done later
    if data_good == True:
        data["valid"] = True
    else:
        data["valid"]      = False
        data["erorr_message"] = erorr_message
    return data

def validateFinalRegisterData(name,nationalId,phone,password):
    data_good     = True
    erorr_message = ""
    data          = {}
    # tobe done later
    if data_good == True:
        data["valid"] = True
    else:
        data["valid"]      = False
        data["erorr_message"] = erorr_message
    return data



def mobileErorrResponse(responseStatusId,message):
    data = {"responseStatusId":str(responseStatusId), "message":message}
    return data

class getAreas(APIView):
    def get(self, request):
        data2 = Area.objects.all()
        arr = []
        for data1 in data2:
            arr.append(data1.name)
        return Response(arr)

class request_service(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        client_id   = data2["clientId"]
        service_id   = data2["serviceId"]
        try:
            client  = Client.objects.get(id=client_id)
            service = SimpleService.objects.get(eNum=service_id)
            x       = RequestSimpleService.objects.create(client=client, service=service)
            data = {"responseStatusId":"1", "message":"تم استقبال طلبك, سيتم التواصل معك قريبا"}
        except Exception as e:
            data = {"responseStatusId":"2", "message":"erorr happens"}
        return Response(data)

class contact_us(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        client_id   = data2["clientId"]
        requestTypeId   = data2["serviceId"]
        # typee = request_service
        # requestType = checkReuestType(url)
        if requestTypeId   == "3" : # " suggest":
            msg = "اقتراحك"
        elif requestTypeId ==  "2" : #   ask":
            msg = "استفسارك"
        elif requestTypeId ==  "1" : #   complaint":
            msg = "شكواك"
        data = {"responseStatusId":"1","message":f"تم تلقى {msg}, ستم التواصل معك قريبا"}
        return Response(data)

class profileImage(APIView):
    def get(self, request):
        data2=json.loads(request.body)
        client_id   = data2["clientId"]
        image = Client.objects.get(id=client_id).image
        data = {"responseStatusId":"1" , "image":image.url}
        return Response(data)

    def post(self, request):
        data2=json.loads(request.body)
        client_id   = data2["clientId"]
        image1      = request.FILES.get
        return Response(data2)

class offers(APIView):
    def get(self, request):
        offers = Offers.objects.all()
        offersData = []
        for offer in offers:
            offersData.append(offer.image.url)
            # offer.image.url
        data = offersData
        return Response(data)

class activate(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        client_id   = data2["clientId"] if 'clientId' in data2 else None
        if client_id:
            client=Client.objects.get(id=client_id)
            client.activation_request = True
            client.save()
            data = {"responseStatusId": "1",'message':'تم تفعيل الخدمة'}
        else:
            data = {'message':'erorr happens'}
        return Response(data)

class profile_edit(APIView):
    def post(self, request):
        data2       = json.loads(request.body)
        client_id   = data2["id"]
        if client_id:
                client=Client.objects.get(id=client_id)
                area = Area.objects.filter(name=data2["area"])
                client.area= client.area
                client.password=data2["password"]              if 'password' in data2 else client.password
                client.streetName=data2["streetName"]          if 'streetName' in data2 else client.password
                client.phone=data2["phone"]                    if 'phone' in data2 else client.phone
                client.addressBuilding=data2["buildingNumber"] if 'buildingNumber' in data2 else client.addressBuilding
                client.addressApartment=data2["apartementNumber"] if 'apartementNumber' in data2 else client.addressApartment
                client.addressDetails=data2["addressDetails"]     if 'addressDetails' in data2 else client.addressDetails
                client.save()
                data ={'clientId':client.id, 'name':client.name, 'phone':client.phone,'nationalId':client.nationalId, 'area':client.area.name, 'streetName':client.streetName, 'buildingNumber':client.addressBuilding,'apartementNumber':client.addressApartment,'addressDetails':client.addressDetails,'registerd_at':client.created_at_date}
        else:
            data = {'message':'erorr happens'}
        return Response(data)


class profile_view(APIView):
    def get(self, request):
        data2       = json.loads(request.body)
        client_id   = data2["id"]
        if client_id:
                client=Client.objects.get(id=client_id)

                data ={'clientId':client.id, 'name':client.name, 'phone':client.phone,'nationalId':client.nationalId, 'area':client.area.name, 'streetName':client.streetName, 'buildingNumber':client.addressBuilding,'apartementNumber':client.addressApartment,'addressDetails':client.addressDetails,'registerd_at':client.created_at_date}
        else:
            data = {'message':'erorr happens'}
        return Response(data)



import json
class registerFirstStep(APIView):
    # check if user is regitered before or not
    def post(self, request):
        data2            = json.loads(request.body)
        print(f"data from front is ${data2}")
        print(f"password from front is ${data2['password']}")
        phone            = data2["phone"]
        nationalId       =  data2["nationalId"]
        password         = data2["password"]
        phoneRight       = Client.objects.filter(phone=phone).count()
        nationalIdRight  = Client.objects.filter(nationalId=nationalId).count()
        client = Client.objects.filter(phone=phone,password=password)
        if phoneRight>0:
            data = mobileErorrResponse(2, "رقم التليفون مرتبط بحساب, الرجاء تسجيل الدخول")
        elif nationalIdRight>0:
            data = mobileErorrResponse(3,"برجاء مراجعة الرقم القومى مرة إخرى, او التواصل مع خدمة العملاء")
        else:
            name             =  data2["name"]
            nationalId       =  data2["nationalId"]
            validateData = validateFirstRegisterData(name,nationalId,phone,password)
            isValid = validateData["valid"]
            if isValid:
                client   = Client.objects.create(name=name,phone=phone,nationalId=nationalId, password=password)
                clientId = client.id
                data = {"responseStatusId":"1", "clientId":str(clientId)}
        return Response(data)

class registerFinal(APIView):
    def post(self, request):
        data2       = json.loads(request.body)
        try:
            client_id   = data2["clientId"]
        except :
            data = mobileErorrResponse(2, "مشكلة برقم العميل")
            print(f"client id erorr in")
            return Response(data)
        print(f"client_id is {client_id}")
        print(f"\n data from front is : {data2}")
        try:
            userc       = Client.objects.filter(id=client_id).count()
            if int(userc) == 1:
                client                  =  Client.objects.get(id=client_id)
                client.area             =  Area.objects.filter(name=(data2["area"])).first()
                client.streetName       =  data2["streetName"] if 'streetName' in data2 else ''
                client.addressBuilding  =  data2["buildingNumber"] if 'buildingNumber' in data2 else ''
                client.addressApartment =  data2["apartementNumber"] if 'apartementNumber' in data2 else ''
                client.addressDetails   =  data2["addressDetails"] if 'addressDetails' in data2 else ''
                client.outsource        = True
                client.save()
                client_id = client.id
                data = clientDataForMobile(client_id, 'register')
        except:
            data = mobileErorrResponse(2, "مشكلة بالبيانات المرسلة")
            print(f"cliet data getting erorr")
            return Response(data)
        if int(userc) == 0:
            data = mobileErorrResponse(2, "برجاء إعادة عملية التسجيل, أو التواصل مع خدمة العملاء")
        else:
            data = {"erorr":int(userc)}
        return Response(data)

class login(APIView):
    def post(self, request):
        data2       = json.loads(request.body)
        phone       = data2["phone"]
        password    = data2["password"]

        PhoneRight = Client.objects.filter(phone=phone)
        users      = Client.objects.filter(phone=phone, password=password)
        if users.count()>0:
            user=users.first()
            userId=user.id
            access_token  = create_access_token(userId)
            refresh_token = create_refresh_token(userId)

            data = clientDataForMobile(userId, 'login', access_token)
            response = Response()
            response.data = data
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
            return response

        elif PhoneRight.count()>0:
            data = mobileErorrResponse(2,"هذا الهاتف مسجل من قبل, اذا كنت نسيت كلمة السر ,الرجاء التواصل مع خدمة العملاء")
            return Response(data)
        else:
            data = mobileErorrResponse(3,"هذا الرقم غير مسجل , الرجاء التسجيل ")
            return Response(data)