from django.urls import path, include
from .views import *

# router = routers.DefaultRouter()
# router.register(r'clients', views.get_clients_api_with_serialization)
app_name = "api"

urlpatterns = [
    path('', index, name='index'),
    path('addClient', addClient.as_view(),name="addClient"),
    path('viewClients', getClients.as_view(), name="viewClients"),
    path('viewClientBySerialNum/<int:serialNum>', getClientBySerialNum.as_view(), name="viewClientBySerialNum")
    # path('addClient', addClient.as_view()),
    #<int:service_id>'
]