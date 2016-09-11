# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160911_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(to='product.Product'),
            preserve_default=True,
        ),
    ]
