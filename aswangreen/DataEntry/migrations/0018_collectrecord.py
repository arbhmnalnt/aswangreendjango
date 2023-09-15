# Generated by Django 4.0.6 on 2023-04-30 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0017_payhistory_receiptnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('serial', models.PositiveIntegerField(blank=True, null=True, verbose_name='رقم الدفتر')),
                ('receiptNum', models.PositiveIntegerField(blank=True, null=True, verbose_name='عدد الايصالات')),
                ('collectOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DataEntry.collectorder', verbose_name='طلب التحصيل')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]