# Generated by Django 4.0.6 on 2022-12-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0045_employee_email_employee_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
