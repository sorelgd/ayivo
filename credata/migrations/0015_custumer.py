# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0014_auto_20161016_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('last_name', models.CharField(help_text='Saisir le nom de famille', max_length=64, verbose_name='Nom de famille')),
                ('first_name', models.CharField(help_text='Entrez les pr\xe9noms', max_length=64, verbose_name='Pr\xe9noms')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('sex', models.CharField(choices=[('nome', 'NONE'), ('M', 'Masculin'), ('F', 'Feminin')], default='none', max_length=1, verbose_name='Sexe')),
                ('pref_contry', models.CharField(blank=True, help_text='Prefixe pays', max_length=4, verbose_name='Prefixe Pays')),
                ('tel', models.CharField(help_text='Votre num\xe9ro de t\xe9l\xe9phone', max_length=12, verbose_name='T\xe9l\xe9phone')),
                ('address', models.CharField(blank=True, help_text='Rue 31 Avenue Steimeiz', max_length=256, verbose_name='Adresse')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('is_admin', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('country_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='credata.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]