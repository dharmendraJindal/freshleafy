# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_orderedproduct_userordersummary'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userordersummary',
            name='ordered_product',
        ),
        migrations.RemoveField(
            model_name='userordersummary',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserOrderSummary',
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='user_order',
            field=models.ForeignKey(blank=True, to='product.UserOrder', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.OneToOneField(to='product.Product'),
            preserve_default=True,
        ),
    ]
