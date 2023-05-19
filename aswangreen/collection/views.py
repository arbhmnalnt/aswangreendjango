from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import *
from DataEntry.models import *
from django.core import serializers as core_serializers

import datetime
from datetime import datetime
import json
# Create your views here.


class GetClientToCollectFrom(APIView):
    def post(self, request):
        data2=json.loads(request.body)
        area = data2["area"]
        areaCount = Area.objects.filter(name=area).count()
        if areaCount>0:
            data = get_client_to_collect_from(area)
        else:
            data = get_client_to_collect_from(area='all')
        return Response(data)
        # return Response ({'areaCount': areaCount})


# ============================== FUNCTIONS PART ==================
def get_unic(follows_list):
    # make a unic dictionary
    follow_dict = {}
    follow_unic_list
    for follow in follow_list:
        pass
    return data
#    date_examplea = {'contractDate','id', 'name', 'clientPhone', 'area', total_required}

def get_client_to_collect_from(area):
    data_list = []
    data_object = {}
    data = {}
    if area !='all':
        follows = FollowContractServices.objects.filter(collcetStatusNums='مطلوب الدفع', client__area__name=area)
    # else:
    #     follows = FollowContractServices.objects.filter(collcetStatusNums='مطلوب الدفع')
    # temp = follows.coun()
    if follows.count() > 0:
        for follow in follows:
            if follow.service.typee == "مستمر":
                temp={}
                temp["id"] = follow.client.id
                temp['contractDate'] = Contract.objects.get(client=follow.client).created_at_date
                temp["area"]   = area
                temp["clientName"]   = follow.client.name
                temp["phone"]  = follow.client.phone
                temp["serial"] = follow.client.serialNum
                temp["deserved"]  = follow.service.price
                data_list.append(temp)
            else:
                continue
        data = data_list
        # data = get_unic(data_list)
        # data = {'name':area}
    else:
        data = {'msg': follows.count()}
    return data
