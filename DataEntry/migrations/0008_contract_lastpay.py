# Generated by Django 4.0.6 on 2023-04-17 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0007_client_customfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='lastPay',
            field=models.DateField(blank=True, null=True),
        ),
    ]