# Generated by Django 4.2.3 on 2023-09-21 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0039_client_collectdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='services',
        ),
    ]