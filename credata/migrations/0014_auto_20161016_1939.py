# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0013_auto_20161016_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='is_couvrage',
            field=models.BooleanField(default=False, verbose_name='Couverture'),
        ),
    ]
