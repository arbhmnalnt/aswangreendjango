# Generated by Django 4.0.6 on 2022-10-02 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0022_client_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='addressArea',
            new_name='area',
        ),
    ]
