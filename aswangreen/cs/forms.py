from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


from .models import Service, Client, Order, Request

class ServiceForm(forms.ModelForm):
    name    =   forms.CharField(label="اسم الخدمة")
    price   =   forms.IntegerField(label="السعر")
    # cost   =   forms.IntegerField(label="التكلفة")
    notes   =   forms.CharField(label="ملاحظات", widget=forms.Textarea)
    
    class Meta:
        model = Service
        fields = ['name', 'price', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('price'),
            Field('cost'),
            Field('notes'),
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):
    name    =   forms.CharField(label="اسم العميل")
    phone   =   forms.CharField(label="رقم التليفون")
    addressDetails = forms.CharField(label="العنوان بالتفصيل", widget=forms.Textarea)
    notes   =   forms.CharField(label="ملاحظات", widget=forms.Textarea)

    def save(self, commit=True, user=None):
        client = super().save(commit=False)
        if user:
            client.created_by = user
        if commit:
            client.save()
        return client

    class Meta:
        model = Client
        fields = ['name', 'phone', 'addressDetails', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
            Field('phone'),
            Field('addressDetails'),
            Field('notes'),
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'service',  'DueDate', 'Status')
        labels = {
            'client'  : 'العميل' ,
            'service' : 'الخدمة' ,
            'Status'  : 'حالة الطلب',
            'DueDate' : 'تاريخ اداء الخدمة',
        }

        widgets = {
            'client'  : forms.Select(attrs={'class': 'form-control'}),
            'service' : forms.Select(attrs={'class': 'form-control'}),
            'Status'  : forms.Select(attrs={'class': 'form-control'}),
            'DueDate' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('client'),
            Field('service'),
            Field('Status'),
            Field('DueDate'),
            
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['client', 'kind', 'body']
        labels = {
            'client'  : 'العميل' ,
            'kind' : 'نوع الطلب' ,
            'body'  : 'التفاصيل'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('client'),
            Field('kind'),
            Field('body'),
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'