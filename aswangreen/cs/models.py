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

class Service(TimeStampMixin,models.Model):
    name                     = models.CharField(max_length=50,null=True, blank=True)
    price                    = models.IntegerField(null=True, blank=True)
    # cost                     = models.IntegerField(null=True, blank=True)
    notes                    = models.TextField(max_length=250,null=True, blank=True)


class Client(TimeStampMixin,models.Model):
    name            = models.CharField(max_length=100,null=True, blank=True, db_index=True)
    phone           = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    addressDetails  = models.TextField(max_length=250,null=True, blank=True, help_text="العنوان بالتفصيل")
    created_by      = models.ForeignKey('DataEntry.Employee', related_name='employee_created_by', on_delete=models.CASCADE,null=True, blank=True)
    notes           = models.TextField(max_length=250,null=True, blank=True)

class Order(TimeStampMixin,models.Model):
    STATUS = (
        ('OR', 'تم تلقى الطلب'),   #   Order Recived
        ('OIP', 'جارى تنفيذ الطلب'),   # Order in Progress
        ('OCD', 'تم تنفيذ الطلب'),   #  Order Confirmed Done        
    )
    client               = models.ForeignKey('Client', related_name='client', on_delete=models.CASCADE,null=True, blank=True)
    service              = models.ForeignKey('Service', related_name='service', on_delete=models.CASCADE,null=True, blank=True)
    DueDate              = models.DateField(null=True, verbose_name="تاريخ اداء الخدمة")
    Status               = models.CharField(max_length=5,null=True, choices=STATUS, default = 'OR') 


class Request(TimeStampMixin, models.Model):
    KIND = (
        ('C', 'شكوى'),  # complaint
        ('S', 'اقتراح'), # suggestion
        ('R', 'طلب'),    # request
    )
    client          = models.ForeignKey('Client', related_name='requestClient', on_delete=models.CASCADE,null=True, blank=True)
    kind            = models.CharField(max_length=5,null=True, choices=KIND, default = 'OR') 
    body            = models.TextField(max_length=500, null=True)
    created_by      = models.ForeignKey('DataEntry.Employee', related_name='request_created_by', on_delete=models.CASCADE,null=True, blank=True)
