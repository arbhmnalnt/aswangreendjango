# Generated by Django 4.0.6 on 2023-05-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0023_rename_prevdate_payhistory_ecd'),
    ]

    operations = [
        migrations.CreateModel(
            name='collectionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serial', models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر')),
                ('receiptNum', models.PositiveIntegerField(blank=True, null=True, verbose_name='عدد الايصالات')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='collectrecord',
            name='receiptNum',
        ),
        migrations.RemoveField(
            model_name='collectrecord',
            name='serial',
        ),
        migrations.AddField(
            model_name='collectrecord',
            name='collectionRecord',
            field=models.ManyToManyField(related_name='services', to='DataEntry.collectionrecord'),
        ),
    ]
