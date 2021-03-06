# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_user', models.BooleanField(default=True, verbose_name='Utilisateur simple')),
                ('is_contact', models.BooleanField(default=False, verbose_name='Utilisateur simple')),
                ('sex', models.CharField(choices=[('nome', 'NONE'), ('M', 'Masculin'), ('F', 'Feminin')], default='none', max_length=1, verbose_name='Sexe')),
                ('lastname', models.CharField(help_text='Saisir le nom de famille', max_length=64, verbose_name='Nom de famille')),
                ('firstname', models.CharField(help_text='Entrez les pr\xe9noms', max_length=64, verbose_name='Pr\xe9noms')),
                ('tel', models.CharField(help_text='Votre num\xe9ro de t\xe9l\xe9phone', max_length=12, verbose_name='T\xe9l\xe9phone')),
                ('address', models.CharField(blank=True, help_text='Rue 31 Avenue Steimeiz', max_length=256, verbose_name='Adresse')),
                ('is_customer', models.BooleanField(default=True, verbose_name='Actif')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('nome', 'NONE'), ('M', 'Masculin'), ('F', 'Feminin')], default='none', max_length=1, verbose_name='Sexe')),
                ('name', models.CharField(help_text='Saisir le nom de famille', max_length=64, verbose_name='Nom de famille')),
                ('firstname', models.CharField(help_text='Entrez les pr\xe9noms', max_length=64, verbose_name='Pr\xe9noms')),
                ('username', models.CharField(max_length=24, verbose_name='Compte de connexion')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('pref_contry', models.CharField(blank=True, help_text='Prefixe pays', max_length=4, verbose_name='Prefixe Pays')),
                ('tel', models.CharField(help_text='Votre num\xe9ro de t\xe9l\xe9phone', max_length=12, verbose_name='T\xe9l\xe9phone')),
                ('address', models.CharField(blank=True, help_text='Rue 31 Avenue Steimeiz', max_length=256, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('is_contact', models.BooleanField(default=True, verbose_name='Utilisateur simple')),
                ('is_user', models.BooleanField(default=False, verbose_name='Utilisateur simple')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
