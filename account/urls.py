from django.urls import path, include
from .views import *
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import viewsets, status


app_name = "account"


urlpatterns = [
    path('activate', activate.as_view(), name='activate'),
    path('request_service', request_service.as_view(), name='request_service'),
    path('contact_us', contact_us.as_view(), name='contact_us'),
    path('offers', offers.as_view(), name='offer' ),
    path('getAreas',getAreas.as_view(), name='getAreas'),
    #//
    path('profile/img', profileImage.as_view(), name='profile_img'),
    path('profile/edit', profile_edit.as_view(), name='profile_edit'),
    path('profile/view', profile_view.as_view(), name='profile_view'),
    path('registerFirstStep', registerFirstStep.as_view(), name='registerFirstStep'),
    path('registerFinal', registerFinal.as_view(), name='registerFinal'),
    path('login', login.as_view(), name='login'),
    # ///
    path('user', UserAPIView.as_view(), name='UserAPIView'),
    # path('user', UserAPIView.as_view(), name='UserAPIView'),
    path('refresh', RefreshAPIView.as_view(), name='refresh'),
    path('logout', LogoutAPIView.as_view(), name='logout')
]