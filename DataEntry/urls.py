from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'clients', views.get_clients_api_with_serialization)

app_name="DataEntry"

urlpatterns = [
    # -- temp pages
    path('', TmainPage, name="mainPage") ,
    path('TmainPage/', TmainPage, name="TmainPage") ,
    path('TnewContract/', TnewContract, name="TnewContract"),
    path('checkClientSerial/', checkClientSerial, name="checkClientSerial"),

    # --- end temp pages
    path('', index, name='index'),
    path('filters' ,filters.as_view(), name='filters'),
    path('contractTables', contractTables.as_view(), name='collection_stats'),
    path('getServices' ,getServices.as_view(), name='getServices'),
    path('getRegions' ,getRegions.as_view(), name='getRegions'),
    # --
    path('addNewContract' ,addNewContract.as_view(), name='addNewContract'),
    path('handleClients' ,HandleClients.as_view(), name='HandleClients'),

    # main_page_apis
    path('mainPageStatsFirst', mainPageStatsFirst.as_view()),
    path('mainPageStatsSecond', mainPageStatsSecond.as_view()),
    path('mainPageStatsThird', mainPageStatsThird.as_view()),
    # new contract page apis

    path('newContractPageFirst', missingOrUnfinishedRequests.as_view()),

    # third page apis  # cuurent contracts
    path('currentContractCount', currentContractCount.as_view()),
    path('currentContractTable', currentContractTable.as_view()),
    path('currentContractTableEditContrctServices', currentContractTable.as_view()),
    path('currentContractTableViewClientProfile', currentContractTableViewClientProfile.as_view()),
    # path('currentContractTableSearch', currentContractTableSearch.as_view()),
    # path('currentContractTableFilter', currentContractTableFilter.as_view()),
    #path('currentContractTableCancelContract', currentContractTableCancelContract.as_view()),

    ## forth page apis   # make collect order page

    path('getUnPaidClientsNum', getUnPaidClientsNum.as_view()),
    path('UnPaidClientsTable', UnPaidClientsTable.as_view()),


    # make new collect order
    path('newCollectOrder', newCollectOrder.as_view()),

    # some features and standalone

    ##
    ## get follow contracts by one key filter or more
    path('filterFollowContracts', filterFollowContractServicesRecord),
    #### ---
    ## 2- generateFilteredTableView
    path('generateFilteredTableView', generateFilteredTableView.as_view())
    # 1- search and get client or clients by one key or more
]



# path('get_clients_api', get_clients_api.as_view(), name='get_client_api'),
# path('get_clients_api_with_serialization', get_clients_api_with_serialization.as_view({'get': 'list'}), name='get_clients_api_with_serialization'),
# path('get_client_services_api_with_serialization/<int:client_id>', get_client_services_api_with_serialization.as_view(), name='get_client_services_api_with_serialization'),
# path('get_service_details_api/<int:service_id>', get_service_details_api.as_view(), name='get_service_details_api'),
# path('get_client_services_api/<int:client_id>', get_client_services_api, name='get_client_services_api')