from django.urls import path, include
from .views import *
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import viewsets, status


app_name = "collection"


urlpatterns = [
    path('getClientToCollectFrom', GetClientToCollectFrom.as_view(), name='getClientToCollectFrom'),
]