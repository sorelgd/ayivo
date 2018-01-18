# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from credata.models import Country



#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.db import models
#from ayivo.credata.models import Country


# Create your models here.
class Person(models.Model):

    list_sex = (
        ('nome', 'NONE'),
        ('M', u'Masculin'),
        ('F', u'Feminin'),
    )
    sex = models.CharField('Sexe', choices=list_sex, max_length=1, default='none')
    name = models.CharField(u'Nom de famille', max_length=64, blank=False, help_text=u'Saisir le nom de famille')
    firstname = models.CharField(u'Prénoms', max_length=64, blank=False, help_text=u'Entrez les prénoms')
    is_active = models.BooleanField('Actif', default=True)
    country_id = models.ForeignKey('credata.Country',blank=True,)
    pref_contry = models.CharField(u'Prefixe Pays', max_length=4, blank=True, help_text='Prefixe pays')
    tel = models.CharField(u'Téléphone', max_length=12, blank=False, help_text=u'Votre numéro de téléphone')
    address = models.CharField(u'Adresse', max_length=256, blank=True, help_text='Rue 31 Avenue Steimeiz')
    email = models.EmailField(max_length=50, blank=True)
    ##user = models.OneToOneField(User, related_name='user')
    class Meta:
        abstract = True


# class Custumer(Person):
#     username = models.CharField(u'Compte de connexion', max_length=24, blank=False, help_text=u'')
#     is_custumer = models.BooleanField('Client', default=True)
#     is_contact = models.BooleanField('Contact d\'un client', default=False)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    ##bio = models.TextField(max_length=500, blank=True)
    #location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)

    # def __unicode__(self):
    #     return u'%s %s' % (self.name.upper(), self.firstname.capitalize())


class Custumer(User):
    list_sex = (
        ('nome', 'NONE'),
        ('M', u'Masculin'),
        ('F', u'Feminin'),
    )
    sex = models.CharField('Sexe', choices=list_sex, max_length=1, default='none')
    address = models.CharField(u'Adresse', max_length=256, blank=True, help_text='Rue 31 Avenue Steimeiz')
    tel = models.CharField(u'Téléphone', max_length=12, blank=False, help_text=u'Votre numéro de téléphone')
    country_id = models.ForeignKey('credata.Country',)
    is_custumer = models.BooleanField('Client', default=True)


    def __unicode__(self):
        return u'%s %s' % (self.last_name.upper(), self.first_name.capitalize())


class CustumerContact(Person):
    is_custumer = models.BooleanField('Client', default=False)
    is_contact = models.BooleanField('Contact d\'un client', default=True)
    custumer_id = models.ForeignKey('Custumer',)

    def __unicode__(self):
        return u'%s %s' % (self.name.upper(), self.firstname.capitalize())


# class Testuser(User):

#     class Meta:
#         proxy = True  # Nous spécifions qu'il s'agit d'un proxy
#         ordering = ["last_name"]  # Nous changeons le tri par défaut


#     def __unicode__(self):
#         return u'%s %s' % (self.last_name.upper(), self.first_name.capitalize())

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Custumer.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.custumer.save()



