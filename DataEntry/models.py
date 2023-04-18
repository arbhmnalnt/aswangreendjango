import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    is_deleted      = models.BooleanField (default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    created_at_date = models.DateField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)
    updated_at_date = models.DateField(auto_now=True,null=True)

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'name'):
            if self.name != None:
                return str(self.name)
            else:
                return str("object")
            # return self.name
        elif hasattr(self, 'image'):
            return str(self.id)

        elif hasattr(self, 'serialNum'):
            return str(self.id)

        elif hasattr(self, 'employees'):
            return f"دفتر حضور يوم :  {self.date}"
        elif hasattr(self, 'title'):
            return str(self.title)
        elif hasattr(self, 'COLLECT_STATUS'):
            return str(self.service)
        elif hasattr(self, 'collector'):
            return str(self.collector)
        elif hasattr(self, 'client'):
                return str(self.client)
        else:
            return str("object_")


class Departement(TimeStampMixin,models.Model):
    name  = models.CharField(max_length=50)
    notes = models.TextField(max_length=50,null=True, blank=True)
    is_test         = models.BooleanField(default=True)


class Employee(TimeStampMixin,models.Model):
        #
    WORKER = "عامل"
    EMPLOYEE = "موظف"
    CHOICES_EMP = (
        (WORKER, "عامل"),
        (EMPLOYEE, "موظف")
    )

    DAILY = "يوميه"
    MONTHLY = "شهرى"
    CHOICES_SALARY_TYPE = (
        (DAILY, "يوميه"),
        (MONTHLY, "شهرى")
    )

    name         = models.CharField(max_length=50 , null=True, blank=True,  verbose_name="الاسم")
    role         = models.CharField(max_length=50 , null=True, blank=True, default=" ")
    job2         = models.CharField(max_length=50 , null=True, blank=True, default=" ") # for abdallah api auth
    email        = models.CharField(max_length=50 , null=True, blank=True,  verbose_name="الايميل")
    password     = models.CharField(max_length=50 , null=True, blank=True,  verbose_name="كلمة السر")
    address      = models.CharField(max_length=50 , null=True, blank=True)
    phone        = models.CharField(max_length=11, null=True, blank=True)
    departement  = models.ForeignKey('Departement', on_delete=models.CASCADE,  null=True, blank=True)
    jobTitle     = models.CharField(max_length=50, null=True, blank=True)
    dateOfEmployment  = models.DateField(null=True, blank=True, verbose_name="تاريخ التعيين")
    created_prev_date = models.DateField(null=True, blank=True)
    dateOfBirth  = models.DateField(null=True, blank=True)
    naId         = models.CharField(max_length=14, null=True, blank=True)
    typee        = models.CharField(max_length=50 , null=True, blank=True, choices=CHOICES_EMP) # will be get front as [ employee or worker ]
    salaryType   = models.CharField(max_length=50 , null=True, blank=True, choices=CHOICES_SALARY_TYPE) # will be get front as [ daily or monthly ]
    salary       = models.IntegerField(null=True, blank=True)
    eNum         = models.IntegerField(null=True, blank=True, unique=True, db_index=True, verbose_name="الرقم التعريفى") # custom employee number for future us as like his id in company or any use else
    notes        = models.TextField(max_length=50,null=True, blank=True)
    is_test      = models.BooleanField(default=True)
    last_login   = models.DateTimeField(null=True, blank=True)



class Typee(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.name

class Service(TimeStampMixin,models.Model):
    name                     = models.CharField(max_length=50,null=True, blank=True)
    typee                    = models.CharField(max_length=50,null=True, blank=True)
    is_main                  = models.BooleanField(default=False)
    price                    = models.IntegerField(default=10)
    notes                    = models.TextField(max_length=250,null=True, blank=True)
    priceType                = models.TextField(max_length=250,null=True, blank=True)
    supervisor               = models.ForeignKey('Employee', related_name='supervisor', on_delete=models.CASCADE,null=True, blank=True)
    billSerial               = models.IntegerField(null=True, blank=True, unique=True)
    billed_at                = models.DateField(null=True, blank=True)
    fixedDeliveryDate        = models.IntegerField(default=1,null=True, blank=True) # check that the day nuumber is between 1-30 in api insert
    fixedPriceCollectDate    = models.IntegerField(default=25,null=True, blank=True) # check that the day nnumber is between 1-30 in api insert
    fixedPriceCollectDate_more    = models.DateField(null=True, blank=True) # may neeed in future use
    is_test         = models.BooleanField(default=True)

class SubService(TimeStampMixin,models.Model):
    baseService       = models.ForeignKey('Service', related_name='Baseservice', on_delete=models.CASCADE,null=True, blank=True)
    name                     = models.CharField(max_length=50,null=True, blank=True)
    typee             =  models.ForeignKey('Typee', on_delete=models.CASCADE,null=True, blank=True)
    price                    = models.IntegerField(null=True, blank=True, default=10)
    

class Area(TimeStampMixin,models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    counter = models.IntegerField(default=0,null=True, blank=True)
    is_test         = models.BooleanField(default=True)

class Client(TimeStampMixin,models.Model):
    # typee           = models.ForeignKey('Typee', on_delete=models.CASCADE,null=True, blank=True)
    serialNum       = models.IntegerField(null=True, blank=True, unique=True, db_index=True, verbose_name="الرقم التعريفى") # custom client number for future us as like his id in company or any use else
    name            = models.CharField(max_length=100,null=True, blank=True, db_index=True)
    phone           = models.CharField(max_length=11, null=True, blank=True, db_index=True)
    password        = models.CharField(max_length=150, null=True, blank=True, db_index=True)
    nationalId      = models.CharField(max_length=14, null=True, blank=True, db_index=True)
    area            = models.ForeignKey('Area', related_name='area', on_delete=models.CASCADE,null=True, blank=True)
    streetName      = models.CharField(max_length=150, null=True, blank=True)
    addressBuilding = models.CharField(max_length=150,null=True, blank=True, help_text="تفاصيل العمارة السكنية")
    addressApartment= models.CharField(max_length=150,null=True, blank=True, help_text="تفاصيل الشقه")
    addressDetails  = models.TextField(max_length=250,null=True, blank=True, help_text="اى تفاصيل إخرى للعنوان")
    customFilter    = models.CharField(max_length=250, null=True, blank=True, help_text="فلتر مخصص")
    contractDate    = models.DateField(null=True, blank=True)  # for clients with older contract date 
    created_prev_date = models.DateField(null=True, blank=True)
    activation_request= models.BooleanField(default=False)
    outsource         = models.BooleanField(default=False)
    created_by      = models.ForeignKey('Employee', related_name='client_created_by_employee', on_delete=models.CASCADE,null=True, blank=True)
    modified_by     = models.ForeignKey('Employee', related_name='client_modified_by_employee', on_delete=models.CASCADE,null=True, blank=True)
    belongs_to      = models.ForeignKey('Employee', related_name='belongs_to_employee' , on_delete=models.CASCADE,null=True, blank=True)
    #
    is_employee       = models.BooleanField(default=False)
    missing_info      = models.BooleanField(default=False)
    #
    activation_request_accepted = models.BooleanField(default=False)  # is user registered from the interface of web or app or from dataentry person
    is_test         = models.BooleanField(default=True)
    contactMe       = models.CharField(max_length=50,null=True, blank=True, default=0)
    image           = models.ImageField(upload_to='images/clients/', default='user_profile_image_placeholer.png')
    notes           = models.TextField(max_length=250,null=True, blank=True)
    #
    deserved        = models.IntegerField(default=0, help_text="إجمالى المستحق على العميل")


class Contract(TimeStampMixin,models.Model):
    serialNum       = models.IntegerField(help_text="رقم سريال متفرد لكل تعاقد",unique=True,null=True, blank=True,db_index=True)
    client          = models.OneToOneField('Client', related_name='contract_client', on_delete=models.CASCADE,null=True, blank=True,db_index=True)
    services        = models.ManyToManyField('Service',related_name='services')
    # subServices     = models.ManyToManyField('SubService',related_name='services')
    belong_to       =  models.ForeignKey('Employee', related_name='contract_getter', on_delete=models.CASCADE,null=True, blank=True)
    created_prev_date = models.DateField(null=True, blank=True)
    lastPay         = models.DateField(null=True, blank=True)
    created_by      = models.ForeignKey('Employee', related_name='created_by_employee', on_delete=models.CASCADE,null=True, blank=True)
    modified_by     = models.ForeignKey('Employee', on_delete=models.CASCADE,null=True, blank=True)
    notes           = models.TextField(max_length=250,null=True, blank=True)
    is_test         = models.BooleanField(default=True)

class FollowContractServices(TimeStampMixin,models.Model):
    #
    PAID_NUM = 'تم الدفع'
    PAYMENT_REQUIRED_NUM = 'مطلوب الدفع'
    COLLECTING_DATE_NUM = 'فى انتظار ميعاد التحصيل'
    COLLECT_STATUS_NUM = (
        (PAID_NUM, 'تم الدفع'),
        (PAYMENT_REQUIRED_NUM, 'مطلوب الدفع'),
        (COLLECTING_DATE_NUM, 'فى انتظار ميعاد التحصيل'),
    )
    #
    DONE = "تم اداء الخدمة"
    NOT_DONE = "لم يتم اداء الخدمة"
    CHOICES_SERV = (
        (DONE, 'تم اداء الخدمة'),
        (NOT_DONE, 'لم يتم اداء الخدمة')
    )

    client               = models.ForeignKey('Client', related_name='client', on_delete=models.CASCADE,null=True, blank=True)
    area                 = models.CharField(max_length=50,null=True, blank=True, default='-')
    service              = models.ForeignKey('Service', related_name='service', on_delete=models.CASCADE,null=True, blank=True)
    startingDate         = models.DateField(null=True, blank=True)
    serviceDueDate       = models.DateField(null=True, blank=True, verbose_name="تاريخ اداء الخدمه")
    serviceCollectDayStart    = models.IntegerField(null=True, blank=True, default=25, verbose_name="تاريخ بدء التحصيل")
    serviceCollectDayEnd    = models.IntegerField(null=True, blank=True, default=5, verbose_name="تاريخ انهاء التحصيل")
    serviceDueStatus     = models.CharField(max_length=50,null=True, blank=True, choices=CHOICES_SERV, default=NOT_DONE, verbose_name="حالة اداء الخدمة")
    collcetStatusNums    = models.CharField(max_length=50,null=True, blank=True, choices=COLLECT_STATUS_NUM, default=COLLECTING_DATE_NUM,db_index=True)
    total_amount         = models.IntegerField(null=True, blank=True, verbose_name="المبلغ المطلوب تحصيله")
    collected_amount     = models.IntegerField(null=True, blank=True, default=0, verbose_name="المبلغ الذى تم تحصيله")
    collected_month      = models.IntegerField(null=True, blank=True, verbose_name="رقم الشهر")
    collected_date      = models.DateField(null=True, blank=True)
    remain_amount        = models.IntegerField(null=True, blank=True, verbose_name="المبلغ المتبقى")
    created_by           = models.ForeignKey('Employee', related_name='employee', on_delete=models.CASCADE,null=True, blank=True)
    created_prev_date    = models.DateField(null=True, blank=True)
    # source_outside       = models.BooleanField(default=False)   # not for any use just for a conflict
    modified_by          = models.ForeignKey('Employee', on_delete=models.CASCADE,null=True, blank=True)
    notes           = models.CharField(max_length=100,null=True, blank=True)
    is_test         = models.BooleanField(default=True)

class CollectOrder (TimeStampMixin,models.Model):
    collector            = models.ForeignKey('Employee', related_name='collector_employee', on_delete=models.CASCADE,null=True, blank=True, verbose_name="المحصل")
    clients              = models.ManyToManyField('Client',related_name='orders_clients', verbose_name="العملاء")
    areas                = models.ManyToManyField('Area',related_name='orders_areas', verbose_name="المناطق")
    month                = models.IntegerField(null=True, blank=True, verbose_name="الشهر")
    confirmed            = models.BooleanField(default=False, verbose_name="تم التأكيد")
    reason               = models.CharField(max_length=100,null=True, blank=True)
    required             = models.IntegerField(default=0, verbose_name="المبلغ المطلوب تحصيله")
    created_prev_date    = models.DateField(null=True, blank=True)
    is_test              = models.BooleanField(default=True)

class SimpleService(TimeStampMixin,models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    eNum = models.IntegerField(default=0,null=True, blank=True)
    is_test         = models.BooleanField(default=True)

class RequestSimpleService(TimeStampMixin,models.Model):
    client = models.ForeignKey('Client', related_name='request_simple_service_client', on_delete=models.CASCADE,null=True, blank=True)
    service = models.ForeignKey('SimpleService', related_name='simple_service', on_delete=models.CASCADE,null=True, blank=True)
    is_test         = models.BooleanField(default=True)

class Offers(TimeStampMixin,models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    is_test         = models.BooleanField(default=True)

class ContactRequestTypes(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    eNum = models.IntegerField(default=0,null=True, blank=True)
    is_test         = models.BooleanField(default=True)

class ContactRequest(TimeStampMixin,models.Model):
    client = models.ForeignKey('Client', related_name='contact_request_client', on_delete=models.CASCADE,null=True, blank=True)
    contactRequest = models.ForeignKey('ContactRequest', related_name='contact_request', on_delete=models.CASCADE,null=True, blank=True)
    is_test         = models.BooleanField(default=True)