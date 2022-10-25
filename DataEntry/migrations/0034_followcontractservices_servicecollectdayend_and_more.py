# Generated by Django 4.0.6 on 2022-10-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0033_client_is_employee_client_missing_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='followcontractservices',
            name='serviceCollectDayEnd',
            field=models.IntegerField(blank=True, default=5, null=True, verbose_name='تاريخ انهاء التحصيل'),
        ),
        migrations.AddField(
            model_name='followcontractservices',
            name='serviceCollectDayStart',
            field=models.IntegerField(blank=True, default=25, null=True, verbose_name='تاريخ بدء التحصيل'),
        ),
        migrations.AlterField(
            model_name='followcontractservices',
            name='collected_amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='المبلغ الذى تم تحصيله'),
        ),
    ]
