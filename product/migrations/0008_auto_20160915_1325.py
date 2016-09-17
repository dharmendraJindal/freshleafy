# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20160911_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userorder',
            name='order_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 13, 25, 56, 810403)),
            preserve_default=True,
        ),
    ]
