# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0003_auto_20160927_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='operatorPrefixe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefixe', models.CharField(help_text='EX 96 ou 92 ou 90.', max_length=2, verbose_name='Nom USSD')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Country')),
                ('operator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Operator')),
            ],
            options={
                'ordering': ['prefixe'],
            },
        ),
    ]