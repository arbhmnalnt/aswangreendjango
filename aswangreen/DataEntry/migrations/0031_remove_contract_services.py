# Generated by Django 4.0.6 on 2023-09-16 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0030_client_collectdate_contract_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='services',
        ),
    ]
