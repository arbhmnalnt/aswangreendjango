from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "cAccounts"

urlpatterns = [
    path('login/', login, name='customLogin'),
    ]