from django.urls import path, include
from .views import *

app_name = "cs"

urlpatterns = [
    ## services urls 
    path('', ServiceListView.as_view(), name='service_list',),
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    # path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    ## Orders Urls
    path('orders/', OrderListView.as_view(), name='order_list',),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),

    ## clients Urls
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),


    ## requests Urls
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('request/create/', RequestCreateView.as_view(), name='request_create'),
    path('request/<int:pk>/update', requestUpdateView.as_view(), name='request_update')
    ]