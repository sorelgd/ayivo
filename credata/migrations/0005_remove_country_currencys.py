# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0004_auto_20161001_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='currencys',
        ),
    ]