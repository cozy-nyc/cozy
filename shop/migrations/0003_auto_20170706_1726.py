# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170705_1437'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('id', 'slug')]),
        ),
    ]
