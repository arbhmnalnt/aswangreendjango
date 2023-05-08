# Generated by Django 4.0.6 on 2023-05-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0019_followcontractservices_collectedconfirmdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='lastReceiptSerial',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='اخر سريال دفع'),
        ),
        migrations.AddField(
            model_name='followcontractservices',
            name='lastReceiptSerial',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='اخر سريال دفع'),
        ),
    ]
