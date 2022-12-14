from django.contrib import admin
from .models import Departement, Employee, Service, Client, Contract, FollowContractServices, Area, CollectOrder,ContactRequest, ContactRequestTypes,Offers,RequestSimpleService,SimpleService
from import_export.admin import ImportExportModelAdmin

class ContactRequestTypesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'eNum')

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

# ///
admin.site.register(ContactRequestTypes, ContactRequestTypesAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(Offers, OffersAdmin)
admin.site.register(SimpleService, SimpleServiceAdmin)
admin.site.register(RequestSimpleService, RequestSimpleServiceAdmin)

# ///

class DepartementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('eNum', 'name', 'departement','jobTitle','salaryType')
    def get_employees(self, obj):
        return " - ".join([employee.name for employee in obj.employees.all()])

class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','name','typee','price','priceType','supervisor','fixedDeliveryDate','fixedPriceCollectDate')

class AreaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name', 'counter')

class ClientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','serialNum','name','phone','area','created_at')

class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','client','get_services','serialNum','created_at')
    # optimizing the query for each service
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('services')

    def get_services(self, obj):
        return " - ".join([service.name for service in obj.services.all()])


class FollowContractServicesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('client','service','startingDate','serviceDueDate','serviceDueStatus','collcetStatusNums','collected_month','remain_amount','created_by','created_at_date')

class CollectOrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('collector', 'created_at')


# Register your models here.

admin.site.register(Departement, DepartementAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(FollowContractServices, FollowContractServicesAdmin)
admin.site.register(CollectOrder, CollectOrderAdmin)




    # def get_services(self, obj):
    #     return str("\n".join([str(p.services) for p in obj.services.all()]))

    # def get_services(self, obj):
        # services = [p.services for p in obj.services.all()]
    #     services_names = [n.name for n in services]
        # return " "+"\n".join([str(a.services) for a in obj.services.all()])
