# Generated by Django 4.0.6 on 2023-04-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0003_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='addressBuilding',
            field=models.CharField(blank=True, help_text='تفاصيل العمارة السكنية', max_length=150, null=True),
        ),
    ]
