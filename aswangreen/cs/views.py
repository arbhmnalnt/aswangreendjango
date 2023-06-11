from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Service, Client, Order , Request
from .forms import ServiceForm , ClientForm , OrderForm, RequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from DataEntry.models import Employee, Client as DClient

######### Functions Part ############

def createAllClients():
    allClients = DClient.objects.all()
    csClientsName = [client.name for client in Client.objects.all()]
    for client in allClients:
        if client.name not in csClientsName:
            newClient = Client.objects.create(
                name            = client.name,
                phone           = client.phone,
                addressDetails  = client.addressDetails,
                created_by      = client.created_by,
                notes           = client.notes,
            )

            # print(f"newClient id => ", newClient.id)
    return newClient

#########  End Functions Part ############


# Create your views here.
## services Views
class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'cs/service_list.html'
    context_object_name = 'services'

    # createAllClients()

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "cs/service_form.html"
    success_url = reverse_lazy('cs:service_list')

class ServiceUpdateView(UpdateView):
    model        = Service
    form_class  = ServiceForm
    template_name = "cs/service_form.html"
    success_url = reverse_lazy('cs:service_list')

## orders Views
class OrderListView(ListView):
    model = Order
    template_name = 'cs/order_list.html'
    context_object_name = 'orders'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'cs/order_form.html'
    success_url = reverse_lazy('cs:order_list')

class OrderUpdateView(UpdateView):
    model           =  Order
    form_class      = OrderForm
    template_name   = "cs/order_form.html"
    success_url     = reverse_lazy('cs:order_list')


## clients views

class ClientListView(ListView):
    model = Client
    template_name = 'cs/client_list.html'
    context_object_name = 'clients'

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'cs/client_form.html'
    success_url = reverse_lazy('cs:order_create')

    def form_valid(self, form):
        form.instance.created_by = Employee.objects.get(pk=2)
        # Employee.objects.get(pk=data2['userId']
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model           = Client
    form_class      = ClientForm
    template_name   = 'cs/client_form.html'
    success_url     = 'cs:client_list'

## request views
class RequestListView(ListView):
    model = Request
    template_name = 'cs/request_list.html'
    context_object_name = 'requests'

class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'cs/request_form.html'
    success_url = reverse_lazy('cs:request_list')

    def form_valid(self, form):
        form.instance.created_by = Employee.objects.get(pk=2)
        # Employee.objects.get(pk=data2['userId']
        return super().form_valid(form)

class requestUpdateView(UpdateView):
    model = Request
    form_class = RequestForm
    template_name = 'cs/request_form.html'
    success_url = reverse_lazy('cs:request_list')

    def form_valid(self, form):
        form.instance.created_by = Employee.objects.get(pk=2)
        # Employee.objects.get(pk=data2['userId']
        return super().form_valid(form)



