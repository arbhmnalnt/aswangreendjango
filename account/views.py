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
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the account index.")
def collectionDay(request):
    return HttpResponse(collection_day)

class register(APIView):
    def post(self, request):
        data = {'resgister request has been recieved'}
        return Response(data)

class login(APIView):
    def post(self, request):
        data = {'login request has been recieved'}
        return Response(data)

