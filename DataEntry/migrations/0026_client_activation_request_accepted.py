# Generated by Django 4.0.6 on 2022-10-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0025_client_is_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='activation_request_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
