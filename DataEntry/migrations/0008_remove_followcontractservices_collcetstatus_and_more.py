# Generated by Django 4.0.6 on 2022-09-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0007_client_created_prev_date_contract_created_prev_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followcontractservices',
            name='collcetStatus',
        ),
        migrations.AlterField(
            model_name='followcontractservices',
            name='collcetStatusNums',
            field=models.IntegerField(blank=True, choices=[(1, 'تم الدفع'), (2, 'مطلوب الدفع'), (3, 'فى انتار ميعاد التحصيل')], db_index=True, default=3, null=True),
        ),
    ]
