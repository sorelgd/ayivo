# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom Categorie')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code Categorie')),
                ('slug', models.SlugField(blank=True, help_text='Unique value for product page URL, created from name.', unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='credata.Category')),
            ],
            options={
                'ordering': ['-name', '-is_active'],
            },
        ),
        migrations.CreateModel(
            name='CodeUssd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Non du code ussd EX: Transfert credit.', max_length=50, verbose_name='Nom USSD')),
                ('code', models.CharField(help_text='Ex: *124#.', max_length=8, unique=True, verbose_name='Code')),
                ('ussd_type', models.CharField(choices=[('nome', 'NONE'), ('credit', 'Tranfert de Cr\xe9dit'), ('money', "Tranfert de d'argent"), ('data', 'Tranfert de data')], default='none', max_length=30, verbose_name='Type Ussd')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom pays')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Code pays')),
                ('indicatif', models.CharField(blank=True, max_length=4, unique=True, verbose_name='Indicatif pays')),
                ('width', models.IntegerField(default=64, verbose_name='Largeur')),
                ('height', models.IntegerField(default=43, verbose_name='Hauteur')),
                ('flag', models.ImageField(blank=True, height_field='height', null=True, upload_to=b'', verbose_name='Drapeau', width_field='width')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom op\xe9rateur')),
                ('code', models.CharField(max_length=8, unique=True, verbose_name='Code op\xe9rateur')),
                ('logo', models.ImageField(blank=True, height_field='height', null=True, upload_to=b'', verbose_name='Logo opr\xe9rateur', width_field='width')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('codeussds', models.ManyToManyField(to='credata.CodeUssd')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Country')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='OperatorPrefixe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='EX 96 ou 92 ou 90.', max_length=2, verbose_name='Prefixe operateur')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Country')),
                ('operator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Operator')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom produit')),
                ('code', models.CharField(max_length=10, verbose_name='R\xe9f\xe9rence')),
                ('icon', models.ImageField(blank=True, upload_to=b'')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='Prix de vente')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Category')),
            ],
            options={
                'ordering': ['-name', '-code', 'category_id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=10, verbose_name='id order')),
                ('operator_id', models.CharField(max_length=10, verbose_name='code ussd')),
                ('country_id', models.CharField(max_length=10, verbose_name='Country code')),
                ('state', models.CharField(choices=[('pending', 'En attente'), ('processing', 'En traitement'), ('completed', 'Complete'), ('failed', 'Echouer')], default='pending', max_length=30, verbose_name='Type Ussd')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'ordering': ['-order_id', 'country_id'],
            },
        ),
        migrations.AddField(
            model_name='operator',
            name='prefixes',
            field=models.ManyToManyField(to='credata.OperatorPrefixe'),
        ),
        migrations.AddField(
            model_name='codeussd',
            name='operator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credata.Operator'),
        ),
    ]