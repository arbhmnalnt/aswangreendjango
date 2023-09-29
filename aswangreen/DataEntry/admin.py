from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class TypeeAdmin(admin.ModelAdmin):
    list_display = ('name')

class SubServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('baseService','name', 'typee')

class ContactRequestTypesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'eNum')

class TypeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')

class ContactRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('client', 'contactRequest')

class ContactRequestTypesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'eNum')

class OffersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'image')

class SimpleServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'eNum')

class RequestSimpleServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('client', 'service')

class CollectRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('pk',)



class PayHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'client', 'ecd', 'serial')

class collectionRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'get_collectOrder')

    def get_collectOrder(self, obj):
        return obj

# ///
admin.site.register(Typee, TypeeAdmin)
admin.site.register(ContactRequestTypes, ContactRequestTypesAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(Offers, OffersAdmin)
admin.site.register(SimpleService, SimpleServiceAdmin)
admin.site.register(RequestSimpleService, RequestSimpleServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(collectionRecord, collectionRecordAdmin)


# ///

class DepartementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('eNum', 'name', 'departement','jobTitle','salaryType')
    def get_employees(self, obj):
        return " - ".join([employee.name for employee in obj.employees.all()])

class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['delete']
    list_display = ('id','name' ,'price')
    search_fields = ['name', 'id']

class AreaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'counter')

class ClientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'serialNum']
    list_display = ('id','serialNum','name','phone','area','created_at')

class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['client__name', 'client__serialNum']
    list_display = ('id','client','serialNum','created_at')

    def getService(self, obj):
        serviceId = object.service
        service = Service.objects.get(pk=serviceId)
        return str(service.name)

class FollowContractServicesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk','client__name', 'client__area__name']
    list_display = ('client','get_area','service','ecd', 'collcetStatus', 'deservedAmount', 'collectedAmount', 'collectedDate', 'created_by')

    def get_area(self, obj):
        return obj.client.area.name

class CollectOrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('collector', 'get_clients', 'get_areas', 'month', 'confirmed','required', 'created_at',)

    def get_areas(self, obj):
        return " - ".join([area.name for area in obj.areas.all()])

    def get_clients(self, obj):
        return " - ".join([client.name for client in obj.clients.all()])


# Register your models here.

admin.site.register(Departement, DepartementAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(FollowContractServices, FollowContractServicesAdmin)
admin.site.register(CollectOrder, CollectOrderAdmin)
admin.site.register(CollectRecord, CollectRecordAdmin)
admin.site.register(PayHistory,  PayHistoryAdmin)




    # def get_services(self, obj):
    #     return str("\n".join([str(p.services) for p in obj.services.all()]))

    # def get_services(self, obj):
        # services = [p.services for p in obj.services.all()]
    #     services_names = [n.name for n in services]
        # return " "+"\n".join([str(a.services) for a in obj.services.all()])
