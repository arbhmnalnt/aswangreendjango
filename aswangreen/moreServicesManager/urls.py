from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'clients', views.get_clients_api_with_serialization)

app_name="moreServicesManager"

urlpatterns = [
    # -- temp pages
    path('', main, name="mainPage") ,
    # path('add/', addService, name="TmainPage") ,

]