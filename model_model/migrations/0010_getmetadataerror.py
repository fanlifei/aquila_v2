# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_model', '0009_auto_20170622_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetMetaDataError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_ip', models.CharField(max_length=50)),
                ('error_msg', models.CharField(max_length=1000)),
                ('r_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
