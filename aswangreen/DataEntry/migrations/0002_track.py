# Generated by Django 4.2.3 on 2023-09-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at_date', models.DateField(auto_now=True, null=True)),
                ('details', models.TextField(blank=True, max_length=350, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]