# Generated by Django 4.0.6 on 2022-09-26 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0003_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='addressArea',
            field=models.ForeignKey(blank=True, help_text='تفاصيل العمارة السكنية', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='DataEntry.area'),
        ),
        migrations.AlterField(
            model_name='client',
            name='addressBuilding',
            field=models.CharField(blank=True, help_text='تفاصيل العمارة السكنية', max_length=50, null=True),
        ),
    ]
