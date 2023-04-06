from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import viewsets, status as st
from DataEntry.models import *
from django.core import serializers as core_serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


today = datetime.now()
todayDate = datetime.today().strftime("%Y-%m-%d")  #this is used in the page
todayUser = datetime.today().strftime("%d-%m-%Y")
month = today.month

@login_required
def main(request):
    listcount = 15
    contracts_list = Contract.objects.filter(is_deleted=False).order_by("created_prev_date")

    query       = request.GET.get('q')
    queryDate   = request.GET.get('qd')
    queryStatue = request.GET.get('qs')
    if query:
        contracts_list = Contract.objects.filter(
            Q(client__serialNum__icontains=query)& Q(is_deleted=False) |
            Q(client__name__icontains=query)& Q(is_deleted=False) |  Q(client__area__name__icontains=query)& Q(is_deleted=False)|
            Q(belong_to__name__icontains=query)& Q(is_deleted=False) |Q(notes__icontains=query)& Q(is_deleted=False) |
            Q(created_by__name__icontains=query)& Q(is_deleted=False)|Q(services__name__icontains=query)& Q(is_deleted=False)
        ).distinct()
    if queryDate:
        contracts_list = Contract.objects.filter(created_prev_date=queryDate,is_deleted=False).distinct()
    # pagination section 
    paginator = Paginator(contracts_list, listcount) # 6 posts per page
    page = request.GET.get('page')
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)

    ctx = {'contracts_list':contracts_list, 'contracts':contracts}
    return render(request, 'moreServicesManager/main.html',ctx)