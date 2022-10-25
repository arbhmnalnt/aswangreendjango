# Generated by Django 4.0.6 on 2022-10-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0034_followcontractservices_servicecollectdayend_and_more'),
    ]

    operations = [
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
