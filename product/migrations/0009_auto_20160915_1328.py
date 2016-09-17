# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20160915_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='order_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 13, 28, 40, 30040)),
            preserve_default=True,
        ),
    ]
