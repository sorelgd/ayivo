# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 04:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('credata', '0020_auto_20161029_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nom de famille')),
                ('firstname', models.CharField(max_length=64, verbose_name='Pr\xe9noms')),
                ('sexe', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('A', 'Autre')], default='H', max_length=1)),
                ('tel', models.CharField(help_text='Votre num\xe9ro de t\xe9l\xe9phone sans pr\xe9fixe pays', max_length=12, verbose_name='T\xe9l\xe9phone')),
                ('address', models.TextField(blank=True, max_length=256, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('country_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='credata.Country')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]