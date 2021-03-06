# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 19:56
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('material', models.TextField(blank=True)),
                ('location', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('lastActive', models.DateTimeField(default=django.utils.timezone.now)),
                ('visible', models.BooleanField(default=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='store.Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-lastActive',),
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('slug', models.SlugField(max_length=16)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subCats', to='store.Category')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'subcategories',
                'verbose_name': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountExchanged', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deliveryAddress', models.TextField()),
                ('receiveAddress', models.TextField()),
                ('timeSold', models.DateTimeField(auto_now=True)),
                ('ratingSeller', models.DecimalField(decimal_places=1, max_digits=1)),
                ('ratingBuyer', models.DecimalField(decimal_places=1, max_digits=1)),
                ('isValid', models.BooleanField(default=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='store.Item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='subCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.SubCategory'),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('id', 'slug')]),
        ),
    ]
