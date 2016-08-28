# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'pictures')),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('thumbnail', models.ImageField(max_length=500, null=True, upload_to=b'pictures/thumbs', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
