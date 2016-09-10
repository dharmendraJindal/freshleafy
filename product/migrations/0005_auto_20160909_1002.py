# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20160907_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.CharField(default=1, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default=b'Kg', max_length=200),
            preserve_default=True,
        ),
    ]
