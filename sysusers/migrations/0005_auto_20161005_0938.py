# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysusers', '0004_auto_20161005_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custumer',
            old_name='lastname',
            new_name='name',
        ),
    ]
