# Generated by Django 4.0.6 on 2022-10-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0020_rename_image_offers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='activation_request',
            field=models.BooleanField(default=False),
        ),
    ]
