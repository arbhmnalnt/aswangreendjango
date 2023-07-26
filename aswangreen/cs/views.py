from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Service, Client, Order , Request
from .forms import ServiceForm , ClientForm , OrderForm, RequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from DataEntry.models import Employee, Client as DClient
from django.db.models import Q

# Create your views here.
class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('cs:service_list')
    template_name = 'cs/service_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())

## services Views
class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'cs/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)

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

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(client__name__icontains=search_query) & Q(is_deleted=False)
            )
        return queryset

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


class OrderDeleteView(DeleteView):
    model           = Order
    success_url     = reverse_lazy('cs:order_list')
    template_name   = 'cs/order_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object.is_deleted  = True
        self.object.save()
        return redirect(self.get_success_url())

## clients views

class ClientListView(ListView):
    model = Client
    template_name = 'cs/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) & Q(is_deleted=False)
            )
        return queryset

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

class ClientDeleteView(DeleteView):
    model           = Client
    success_url     = reverse_lazy('cs:client_list')
    template_name   = 'cs/client_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object.is_deleted  = True
        self.object.save()
        return redirect(self.get_success_url())

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

class requestDeleteView(DeleteView):
    model           = Request
    success_url     = reverse_lazy('cs:request_list')
    template_name   = 'cs/request_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object.is_deleted  = True
        self.object.save()
        return redirect(self.get_success_url())


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
