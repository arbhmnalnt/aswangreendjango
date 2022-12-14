# Generated by Django 4.0.6 on 2022-09-26 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('counter', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serialNum', models.IntegerField(blank=True, db_index=True, null=True, unique=True, verbose_name='الرقم التعريفى')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, db_index=True, max_length=11, null=True)),
                ('addressArea', models.CharField(blank=True, max_length=50, null=True)),
                ('addressApartment', models.CharField(blank=True, help_text='تفاصيل الشقه', max_length=50, null=True)),
                ('addressDetails', models.CharField(blank=True, help_text='اى تفاصيل إخرى للعنوان', max_length=50, null=True)),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
                ('addressBuilding', models.ForeignKey(blank=True, help_text='تفاصيل العمارة السكنية', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='DataEntry.area')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('jobTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('dateOfEmployment', models.DateField(blank=True, null=True, verbose_name='تاريخ التعيين')),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('naId', models.CharField(blank=True, max_length=14, null=True)),
                ('typee', models.CharField(blank=True, choices=[('عامل', 'عامل'), ('موظف', 'موظف')], max_length=50, null=True)),
                ('salaryType', models.CharField(blank=True, choices=[('يوميه', 'يوميه'), ('شهرى', 'شهرى')], max_length=50, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('eNum', models.IntegerField(blank=True, db_index=True, null=True, unique=True, verbose_name='الرقم التعريفى')),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
                ('departement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.departement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('typee', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('priceType', models.CharField(blank=True, max_length=50, null=True)),
                ('fixedDeliveryDate', models.IntegerField(blank=True, default=1, null=True)),
                ('fixedPriceCollectDate', models.IntegerField(blank=True, default=1, null=True)),
                ('fixedPriceCollectDate_more', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
                ('providers', models.ManyToManyField(related_name='providers', to='DataEntry.employee')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='DataEntry.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FollowContractServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('startingDate', models.DateField(blank=True, null=True)),
                ('serviceDueDate', models.DateField(blank=True, null=True, verbose_name='تاريخ اداء الخدمه')),
                ('serviceDueStatus', models.CharField(blank=True, choices=[('تم اداء الخدمة', 'تم اداء الخدمة'), ('لم يتم اداء الخدمة', 'لم يتم اداء الخدمة')], default='لم يتم اداء الخدمة', max_length=50, null=True, verbose_name='حالة اداء الخدمة')),
                ('collcetStatus', models.CharField(blank=True, choices=[('تم الدفع', 'Service has been paid already'), ('مطلوب الدفع', 'Payment required for the service'), ('فى انتظار ميعاد التحصيل', 'Waiting for collection date')], db_index=True, default='فى انتظار ميعاد التحصيل', max_length=50, null=True)),
                ('collcetStatusNums', models.IntegerField(blank=True, choices=[(1, 'Service has been paid already'), (2, 'Payment required for the service'), (3, 'Waiting for collection date')], db_index=True, default=3, null=True)),
                ('total_amount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ المطلوب تحصيله')),
                ('collected_amount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ الذى تم تحصيله')),
                ('remain_amount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ المتبقى')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='DataEntry.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='DataEntry.employee')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.employee')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='DataEntry.service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serialNum', models.IntegerField(blank=True, db_index=True, help_text='رقم سريال متفرد لكل تعاقد', null=True, unique=True)),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_client', to='DataEntry.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_employee', to='DataEntry.employee')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.employee')),
                ('services', models.ManyToManyField(related_name='services', to='DataEntry.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
