# Generated by Django 4.0.6 on 2022-09-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0013_collectorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectorder',
            name='clients',
            field=models.ManyToManyField(related_name='clients', to='DataEntry.client'),
        ),
    ]
