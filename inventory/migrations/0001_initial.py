# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-23 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.IntegerField(unique=True)),
                ('connectioncode', models.IntegerField()),
                ('custname', models.CharField(max_length=1000)),
                ('zoneid', models.IntegerField()),
                ('Route', models.IntegerField()),
                ('zonename', models.CharField(max_length=100)),
                ('routename', models.CharField(max_length=100)),
                ('waterpipeline', models.CharField(max_length=100)),
                ('plotnumber', models.CharField(max_length=50)),
                ('balance', models.CharField(max_length=100)),
                ('serialno', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('connectionstatus', models.CharField(choices=[('Active Connection', 'Active Connection'), ('Disconnected', 'Disconnected')], max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentid', models.IntegerField(unique=True)),
                ('receiptno', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('paydate', models.DateField()),
                ('paymentmode', models.CharField(max_length=100)),
                ('connectioncode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customers')),
            ],
        ),
    ]
