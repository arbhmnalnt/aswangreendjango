# Generated by Django 4.0.6 on 2022-09-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0015_service_billserial_service_billed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectorder',
            name='clients',
            field=models.ManyToManyField(related_name='orders_clients', to='DataEntry.client'),
        ),
        migrations.AlterField(
            model_name='collectorder',
            name='collector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collector_employee', to='DataEntry.employee', verbose_name='المحصل'),
        ),
    ]
