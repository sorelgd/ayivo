# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0005_remove_country_currencys'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currencys',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='credata.Currency'),
            preserve_default=False,
        ),
    ]
