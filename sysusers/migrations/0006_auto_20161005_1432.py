# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credata', '0011_auto_20161004_0715'),
        ('sysusers', '0005_auto_20161005_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustumerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('nome', 'NONE'), ('M', 'Masculin'), ('F', 'Feminin')], default='none', max_length=1, verbose_name='Sexe')),
                ('name', models.CharField(help_text='Saisir le nom de famille', max_length=64, verbose_name='Nom de famille')),
                ('firstname', models.CharField(help_text='Entrez les pr\xe9noms', max_length=64, verbose_name='Pr\xe9noms')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super utilisateur')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('pref_contry', models.CharField(blank=True, help_text='Prefixe pays', max_length=4, verbose_name='Prefixe Pays')),
                ('tel', models.CharField(help_text='Votre num\xe9ro de t\xe9l\xe9phone', max_length=12, verbose_name='T\xe9l\xe9phone')),
                ('address', models.CharField(blank=True, help_text='Rue 31 Avenue Steimeiz', max_length=256, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('is_custumer', models.BooleanField(default=False, verbose_name='Client')),
                ('is_contact', models.BooleanField(default=True, verbose_name="Contact d'un client")),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='custumer',
            old_name='country_id',
            new_name='country',
        ),
        migrations.AddField(
            model_name='custumercontact',
            name='custumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysusers.Custumer'),
        ),
    ]
