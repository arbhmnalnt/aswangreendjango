# Generated by Django 4.0.6 on 2023-04-30 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0014_contract_esd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='esd',
            new_name='ecd',
        ),
    ]