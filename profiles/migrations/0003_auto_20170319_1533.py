# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170319_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='New York', max_length=40),
        ),
    ]