from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import *
from django.core import serializers as core_serializers
from .serializers import ContractSerializer, ServiceSerializer, ClientSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# create