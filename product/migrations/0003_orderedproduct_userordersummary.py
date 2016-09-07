# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_product_rateunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('product', models.ForeignKey(to='product.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserOrderSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_timestamp', models.DateTimeField(auto_now=True)),
                ('ordered_product', models.ManyToManyField(to='product.OrderedProduct')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
