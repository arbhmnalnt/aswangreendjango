# Generated by Django 4.0.6 on 2022-10-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0028_client_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='addressDetails',
            field=models.TextField(blank=True, help_text='اى تفاصيل إخرى للعنوان', max_length=250, null=True),
        ),
    ]
