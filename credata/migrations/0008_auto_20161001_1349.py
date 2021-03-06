# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0007_auto_20161001_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Franc CFA.', max_length=24, verbose_name='Nom devise')),
                ('code', models.CharField(help_text='FCFA, \xa3, $ ou \u20ac...', max_length=8, verbose_name='Symbole')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('countrys', models.ManyToManyField(blank=True, to='credata.Country')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='country',
            name='currencys',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='credata.Currency'),
            preserve_default=False,
        ),
    ]
