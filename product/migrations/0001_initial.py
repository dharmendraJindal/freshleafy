# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('image_path', models.CharField(max_length=500, null=True, blank=True)),
                ('rate', models.CharField(default=1, max_length=200)),
                ('unit', models.CharField(default=b'Kg', max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RateUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('product', models.ForeignKey(to='product.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_timestamp', models.DateTimeField(default=datetime.datetime(2017, 9, 30, 18, 50, 43, 911200))),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(to='product.ProductCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(to='product.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='user_order',
            field=models.ForeignKey(blank=True, to='product.UserOrder', null=True),
            preserve_default=True,
        ),
    ]
