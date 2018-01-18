from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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
    username = models.CharField(u'Compte de connexion', max_length=24, blank=False, help_text=u'')
    # is_superuser = models.BooleanField('Super utilisateur', default=False)
    is_active = models.BooleanField('Actif', default=True)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, )
    pref_contry = models.CharField(u'Prefixe Pays', max_length=4, blank=True, help_text='Prefixe pays')
    tel = models.CharField(u'Téléphone', max_length=12, blank=False, help_text=u'Votre numéro de téléphone')
    address = models.CharField(u'Adresse', max_length=256, blank=True, help_text='Rue 31 Avenue Steimeiz')
    email = models.EmailField(max_length=50, blank=True)

    class Meta:
        abstract = True


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_user = models.BooleanField('Utilisateur simple', default=True)
    is_contact = models.BooleanField('Utilisateur simple', default=False)
    list_sex = (
        ('nome', 'NONE'),
        ('M', u'Masculin'),
        ('F', u'Feminin'),
    )
    sex = models.CharField('Sexe', choices=list_sex, max_length=1, default='none')
    lastname = models.CharField(u'Nom de famille', max_length=64, blank=False, help_text=u'Saisir le nom de famille')
    firstname = models.CharField(u'Prénoms', max_length=64, blank=False, help_text=u'Entrez les prénoms')
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, )
    tel = models.CharField(u'Téléphone', max_length=12, blank=False, help_text=u'Votre numéro de téléphone')
    address = models.CharField(u'Adresse', max_length=256, blank=True, help_text='Rue 31 Avenue Steimeiz')
    is_customer = models.BooleanField('Actif', default=True)

    #@property
    def __unicode__(self):
        return u'%s - %s' % [self.lastname, self.firstname]


class UserContact(Person):
    is_contact = models.BooleanField('Utilisateur simple', default=True)
    is_user = models.BooleanField('Utilisateur simple', default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.firstname)

