# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170613_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]