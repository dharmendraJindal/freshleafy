# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_one', models.CharField(max_length=100, null=True, blank=True)),
                ('address_two', models.CharField(max_length=100, null=True, blank=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('landmark', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('pincode', models.CharField(max_length=50, null=True, blank=True)),
                ('phonenumber', models.CharField(max_length=20, null=True, blank=True)),
                ('phonenumber_two', models.CharField(max_length=20, null=True, blank=True)),
                ('company', models.CharField(max_length=100, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
