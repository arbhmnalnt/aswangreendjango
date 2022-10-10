from django.urls import path, include
from .views import *


# router = routers.DefaultRouter()
# router.register(r'clients', views.get_clients_api_with_serialization)
app_name = "api"

urlpatterns = [
    path('', index, name='index'),
    # path('addClient', addClient.as_view(),name="addClient"),
    path('viewClients', getClients.as_view(), name="viewClients"),
    path('viewClientByKey', getClientByKey.as_view(), name="viewClientBySerialNum"),
    path('collectionDate', collectionDay,name="collectionDate"),
    # need to be done today
    ## == Contract routes  [ CRUD OPERTAIONS ]
    path('newContract/', addNewContract.as_view(),name="addNewContract"),
    # = path('viewContractData/', viewContractData.as_view(),name="viewContractData"), # profide contract serial or cllient serial
    # = path('updateContractData/', updateContractData.as_view(),name="updateContractData"),
    # = path('DeleteContract/', DeleteContract.as_view(),name="DeleteContractData"),

    # need to be done later
    ## = Client routes  [ CRUD OPERTAIONS ]
    # = path('newClient/', addNewClient.as_view(),name="addNewClient"),  # case adding first client data then contract data then FollowContract Data
    # = path('viewClientProfile/client_id', viewClientProfile.as_view(),name="viewClientProfile"),
    # = path('updateClientProfileData/client_id', updateClientProfileData.as_view(),name="updateClientProfileData"),
    # = path('deleteClientProfile', hideClientProfile.as_view(),name="view_client_profile"),

    # DATA ENTRY APIS
    # stats APIS
    # path('collection_stats', collection_stats.as_view(), name='collection_stats'),
    # path('contractTables', contractTables.as_view(), name='contractTable'),




    #  just for testing
    # path('testing2', testing2, name="testing2"),
    path('collection_stats', collectionStatsTest.as_view(), name='collection_stats'),
    path('contractTables', contractTables.as_view(), name='collection_stats'),
    path('authUser',authUser.as_view(), name="auth_user_system")
    # url ?key=value
    # path('viewClientBySerialNum/<int:serialNum>', getClientBySerialNum.as_view(), name="viewClientBySerialNum"),
    # path('addClient', addClient.as_view()),
    #<int:service_id>'
]