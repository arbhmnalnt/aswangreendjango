# Generated by Django 4.0.6 on 2022-10-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0026_client_activation_request_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contactMe',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]
