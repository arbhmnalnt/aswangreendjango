# Generated by Django 4.0.6 on 2022-11-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0039_alter_contract_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='deserved',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]