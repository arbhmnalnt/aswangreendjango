from django.urls import path, include
from .views import *

app_name = "cs"

urlpatterns = [
    ## services urls
    path('', ServiceListView.as_view(), name='service_list',),
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('delete/<int:pk>', ServiceDeleteView.as_view(), name='service_delete'),

    ## Orders Urls
    path('orders/', OrderListView.as_view(), name='order_list',),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),

    ## clients Urls
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),


    ## requests Urls
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('request/create/', RequestCreateView.as_view(), name='request_create'),
    path('request/<int:pk>/update', requestUpdateView.as_view(), name='request_update'),
    path('request/delete/<int:pk>/', requestDeleteView.as_view(), name='request_delete'),
    ]