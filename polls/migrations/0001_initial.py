# Generated by Django 4.2.5 on 2023-09-15 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('operation_system', models.CharField(default='', max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('cameras', models.CharField(default=1, max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('desc', models.TextField(default='Samsung or Iphone ?')),
            ],
            options={
                'db_table': 'PhoneModel',
            },
        ),
    ]
