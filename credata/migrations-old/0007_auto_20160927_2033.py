# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0006_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('pending', 'En attente'), ('processing', 'En traitement'), ('completed', 'Complete'), ('failed', 'Echouer')], default='pending', max_length=30, verbose_name='Type Ussd'),
        ),
    ]
