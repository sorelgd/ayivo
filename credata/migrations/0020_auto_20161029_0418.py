# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 04:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0019_auto_20161029_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactuser',
            name='country_id',
        ),
        migrations.RemoveField(
            model_name='contactuser',
            name='profil',
        ),
        migrations.DeleteModel(
            name='ContactUser',
        ),
    ]