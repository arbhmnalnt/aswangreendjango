# Generated by Django 4.0.6 on 2023-05-25 14:41

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
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('counter', models.IntegerField(blank=True, default=0, null=True)),
                ('is_test', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serialNum', models.IntegerField(blank=True, db_index=True, null=True, unique=True, verbose_name='الرقم التعريفى')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, db_index=True, max_length=150, null=True)),
                ('nationalId', models.CharField(blank=True, db_index=True, max_length=14, null=True)),
                ('streetName', models.CharField(blank=True, max_length=150, null=True)),
                ('addressBuilding', models.CharField(blank=True, help_text='تفاصيل العمارة السكنية', max_length=150, null=True)),
                ('addressApartment', models.CharField(blank=True, help_text='تفاصيل الشقه', max_length=150, null=True)),
                ('addressDetails', models.TextField(blank=True, help_text='اى تفاصيل إخرى للعنوان', max_length=250, null=True)),
                ('customFilter', models.CharField(blank=True, help_text='فلتر مخصص', max_length=250, null=True)),
                ('created_prev_date', models.DateField(blank=True, null=True)),
                ('needReview', models.BooleanField(default=False)),
                ('outsource', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('missing_info', models.BooleanField(default=False)),
                ('activation_request_accepted', models.BooleanField(default=False)),
                ('is_test', models.BooleanField(default=True)),
                ('contactMe', models.CharField(blank=True, default=0, max_length=50, null=True)),
                ('image', models.ImageField(default='user_profile_image_placeholer.png', upload_to='images/clients/')),
                ('notes', models.TextField(blank=True, max_length=250, null=True)),
                ('deserved', models.IntegerField(default=0, help_text='إجمالى المستحق على العميل')),
                ('serviceId', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lastReceiptSerial', models.PositiveIntegerField(blank=True, null=True, verbose_name='اخر سريال دفع')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='DataEntry.area')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='collectionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serial', models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر')),
                ('receiptNum', models.PositiveIntegerField(blank=True, default=50, null=True, verbose_name='عدد الايصالات')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollectOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True, verbose_name='الشهر')),
                ('confirmed', models.BooleanField(default=False, verbose_name='تم التأكيد')),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('required', models.IntegerField(default=0, verbose_name='المبلغ المطلوب تحصيله')),
                ('created_prev_date', models.DateField(blank=True, null=True)),
                ('is_test', models.BooleanField(default=True)),
                ('areas', models.ManyToManyField(related_name='orders_areas', to='DataEntry.area', verbose_name='المناطق')),
                ('clients', models.ManyToManyField(related_name='orders_clients', to='DataEntry.client', verbose_name='العملاء')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactRequestTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('eNum', models.IntegerField(blank=True, default=0, null=True)),
                ('is_test', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
                ('is_test', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم')),
                ('role', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('job2', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='الايميل')),
                ('password', models.CharField(blank=True, max_length=50, null=True, verbose_name='كلمة السر')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('jobTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('dateOfEmployment', models.DateField(blank=True, null=True, verbose_name='تاريخ التعيين')),
                ('created_prev_date', models.DateField(blank=True, null=True)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('naId', models.CharField(blank=True, max_length=14, null=True)),
                ('typee', models.CharField(blank=True, choices=[('عامل', 'عامل'), ('موظف', 'موظف')], max_length=50, null=True)),
                ('salaryType', models.CharField(blank=True, choices=[('يوميه', 'يوميه'), ('شهرى', 'شهرى')], max_length=50, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('eNum', models.IntegerField(blank=True, db_index=True, null=True, unique=True, verbose_name='الرقم التعريفى')),
                ('notes', models.TextField(blank=True, max_length=50, null=True)),
                ('is_test', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('departement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.departement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('is_test', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('typee', models.CharField(blank=True, default='شهرى', max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=250, null=True)),
                ('priceType', models.TextField(blank=True, default='شهرى', max_length=100, null=True)),
                ('is_test', models.BooleanField(default=True)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='DataEntry.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SimpleService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('eNum', models.IntegerField(blank=True, default=0, null=True)),
                ('is_test', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Typee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, default=10, null=True)),
                ('baseService', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Baseservice', to='DataEntry.service')),
                ('typee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.typee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestSimpleService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('is_test', models.BooleanField(default=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_simple_service_client', to='DataEntry.client')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='simple_service', to='DataEntry.simpleservice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('ecd', models.DateField(blank=True, null=True)),
                ('month', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='الشهر')),
                ('serial', models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر')),
                ('receiptNum', models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الايصال')),
                ('CollectOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.collectorder')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_pay_history', to='DataEntry.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FollowContractServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('ecd', models.DateField(blank=True, null=True, verbose_name='تاريخ  التحصيل المفترض')),
                ('collcetStatus', models.CharField(blank=True, choices=[('wecd', 'فى انتظار ميعاد التحصيل'), ('pr', 'مطلوب الدفع'), ('pip', 'جارى الدفع'), ('pd', 'تم الدفع'), ('lp', 'متأخر الدفع')], default='wecd', max_length=5, null=True)),
                ('deservedAmount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ المطلوب تحصيله')),
                ('collectedAmount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ الذى تم تحصيله')),
                ('collectedDate', models.DateField(blank=True, null=True, verbose_name='تاريخ التحصيل الفعلى')),
                ('collectedConfirmDate', models.DateField(blank=True, null=True, verbose_name='تاريخ تأكيد التحصيل الفعلى')),
                ('remainAmount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ المتبقى')),
                ('collectMonth', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='شهر التحصيل')),
                ('lastReceiptSerial', models.PositiveIntegerField(blank=True, null=True, verbose_name='اخر سريال دفع')),
                ('CollectRecordSerial', models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='السنة')),
                ('notes', models.CharField(blank=True, max_length=100, null=True)),
                ('is_test', models.BooleanField(default=True)),
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
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serialNum', models.IntegerField(blank=True, db_index=True, help_text='رقم سريال متفرد لكل تعاقد', null=True, unique=True)),
                ('created_prev_date', models.DateField(blank=True, null=True)),
                ('lastPay', models.DateField(blank=True, null=True)),
                ('lastReceiptSerial', models.PositiveIntegerField(blank=True, null=True, verbose_name='اخر سريال دفع')),
                ('ecd', models.DateField(blank=True, null=True, verbose_name='تاريخ الدفع المفترض')),
                ('remainAmount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ المتبقى')),
                ('notes', models.TextField(blank=True, max_length=250, null=True)),
                ('needReview', models.BooleanField(default=False)),
                ('is_test', models.BooleanField(default=True)),
                ('belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_getter', to='DataEntry.employee')),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_client', to='DataEntry.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_employee', to='DataEntry.employee')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.employee')),
                ('services', models.ManyToManyField(related_name='services', to='DataEntry.service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('is_test', models.BooleanField(default=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_request_client', to='DataEntry.client')),
                ('contactRequest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_request', to='DataEntry.contactrequest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollectRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('collectOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.collectorder', verbose_name='طلب التحصيل')),
                ('collectionRecord', models.ManyToManyField(related_name='services', to='DataEntry.collectionrecord')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='collectorder',
            name='collector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collector_employee', to='DataEntry.employee', verbose_name='المحصل'),
        ),
        migrations.AddField(
            model_name='client',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belongs_to_employee', to='DataEntry.employee'),
        ),
        migrations.AddField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_created_by_employee', to='DataEntry.employee'),
        ),
        migrations.AddField(
            model_name='client',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_modified_by_employee', to='DataEntry.employee'),
        ),
    ]
