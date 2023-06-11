from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price')
    search_fields = ('id', 'name') 
admin.site.register(Service, ServiceAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'addressDetails')
    list_filter = ('id', 'name', 'phone')
    search_fields = ('id', 'name') 
admin.site.register(Client, ClientAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'service_name','Status')
    list_filter = ('id', 'client__name', 'service__name', 'Status')
    search_fields = ('id', 'name', 'service__name','Status') 

    def client_name(self, obj):
        return obj.client.name
    
    def service_name(self, obj):
        return obj.service.name
    
admin.site.register(Order, OrderAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'kind', 'created_by_name')
    list_filter = ('id', 'client__name','kind')
    search_fields = ('id', 'client__name', 'kind') 

    def client_name(self, obj):
        return obj.client.name
    
    def created_by_name(self, obj):
        return obj.created_by.name
    
    
admin.site.register(Request, RequestAdmin)

