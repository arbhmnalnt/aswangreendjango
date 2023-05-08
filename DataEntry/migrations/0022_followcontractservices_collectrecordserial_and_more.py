# Generated by Django 4.0.6 on 2023-05-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0021_client_lastreceiptserial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followcontractservices',
            name='CollectRecordSerial',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر'),
        ),
        migrations.AddField(
            model_name='payhistory',
            name='prevDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payhistory',
            name='serial',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر'),
        ),
    ]
