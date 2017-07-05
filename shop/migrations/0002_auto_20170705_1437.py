# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('slug',)]),
        ),
    ]