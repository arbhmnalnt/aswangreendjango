from django.urls import path, include
from .views import *

# router = routers.DefaultRouter()
# router.register(r'clients', views.get_clients_api_with_serialization)
app_name = "api"

urlpatterns = [
    path('', index, name='index'),
    path('addClient', addClient.as_view(),name="addClient"),
    path('viewClients', getClients.as_view(), name="viewClients"),
    path('viewClientByKey', getClientByKey.as_view(), name="viewClientBySerialNum"),

    # collection stats
    path('collection_stats', collection_stats.as_view(), name='collection_stats'),
    path('follow_contract', follow_contract.as_view(), name='follow_contract'),




    # testing
    path('testing2', testing2, name="testing2"),
    # url ?key=value
    # path('viewClientBySerialNum/<int:serialNum>', getClientBySerialNum.as_view(), name="viewClientBySerialNum"),
    # path('addClient', addClient.as_view()),
    #<int:service_id>'
]