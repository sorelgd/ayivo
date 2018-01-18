# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
import uuid
#from sysusers.models import CustumerContact
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.

class Country(models.Model):
    name = models.CharField('Nom pays', max_length=50, )
    code = models.CharField('Code pays', max_length=4, unique=True, )
    indicatif = models.CharField('Indicatif pays', max_length=4, unique=True, blank=True)
    width = models.IntegerField('Largeur', default=64)
    height = models.IntegerField('Hauteur', default=43)
    flag = models.ImageField('Drapeau', null=True, blank=True, width_field="width", height_field="height",upload_to="static/flags/")
    is_active = models.BooleanField('Actif', default=True)
    is_couvrage = models.BooleanField('Couverture', default=False)
    currencys = models.ForeignKey('Currency', on_delete=models.CASCADE, blank=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    def __unicode__(self):
        return self.name.upper()

    class Meta:
        ordering = ["-name"]
        # verbose_name_plural = 'Pays'


class Category(models.Model):
    name = models.CharField(u'Nom Categorie', max_length=50, )
    code = models.CharField('Code Categorie', max_length=10, unique=True, )
    slug = models.SlugField('slug', max_length=50, unique=True, blank=True,
                            help_text='Unique value for product page URL, created from name.')
    description = models.TextField('Description', blank=True)
    parent = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE, )
    is_active = models.BooleanField('Actif', default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # create_uid=
    # update_uid=

    class Meta:
        ordering = ['-name', '-is_active']
        # verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name.capitalize()

        # @models.permalink
        # def get_absolute_url(self):
        #    return ('credata_category', (), { 'category_slug': self.slug })
    # def save(self, *args, **kwargs):
    #     self.name


class Product(models.Model):
    name = models.CharField("Nom produit", max_length=100, )
    code = models.CharField(u"Référence", max_length=10, )
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, )
    icon = models.ImageField(null=False, blank=True,upload_to="static/products")
    price = models.DecimalField("Prix de vente", max_digits=6, decimal_places=0, blank=False, default=00)
    #countrys = models.ManyToManyField(Country, blank=True)
    is_active = models.BooleanField('Actif', default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # create_uid=
    # update_uid=

    class Meta:
        ordering = ['-name', '-code', 'category_id']
        # verbose_name_plural = 'Produits'

    def __unicode__(self):
        return self.name.capitalize()


class CodeUssd(models.Model):
    name = models.CharField(u'Nom USSD', max_length=50, help_text='Non du code ussd EX: Transfert credit.')
    code = models.CharField(u'Code', max_length=8, unique=True, help_text='Ex: *124#.')
    operator_id = models.ForeignKey('Operator', on_delete=models.CASCADE, )
    # country_id=models.ForeignKey('Country',on_delete=models.CASCADE,)
    list_ussd = (
        ('nome', 'NONE'),
        ('credit', u'Tranfert de Crédit'),
        ('money', u'Tranfert de d\'argent'),
        ('data', u'Tranfert de data'),
    )

    ussd_type = models.CharField('Type Ussd', choices=list_ussd, max_length=30, default='none')

    is_active = models.BooleanField('Actif', default=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    def __unicode__(self):
        return self.name.capitalize()

    class Meta:
        ordering = ["-name"]


class OperatorPrefixe(models.Model):
    name = models.CharField(u'Prefixe operateur', max_length=2, help_text='EX 96 ou 92 ou 90.')
    operator_id = models.ForeignKey('Operator', on_delete=models.CASCADE, )
    # country_id = models.ForeignKey('Country', on_delete=models.CASCADE, )
    is_active = models.BooleanField('Actif', default=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.operator_id)

    class Meta:
        ordering = ["name"]


class Operator(models.Model):
    name = models.CharField(u'Nom opérateur', max_length=50, )
    code = models.CharField(u'Code opérateur', max_length=8, unique=True, )
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE, )
    logo = models.ImageField(u'Logo oprérateur', null=True, blank=True, upload_to="static/operators/")
    prefixes = models.ManyToManyField(OperatorPrefixe, blank=True)
    codeussds = models.ManyToManyField(CodeUssd, blank=True)
    is_active = models.BooleanField('Actif', default=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    def __unicode__(self):
        return u'%s - %s' % (self.name.capitalize(), self.country_id.code)

    class Meta:
        ordering = ["-name"]


class Currency(models.Model):
    name = models.CharField(u'Nom devise', max_length=24, help_text='Franc CFA.')
    code= models.CharField(u'Nom devise', max_length=24, help_text='xof, ...')
    symbole = models.CharField(u'Symbole', max_length=8, help_text='FCFA, £, $ ou €...')
    countrys = models.ManyToManyField(Country, blank=True)
    # country_id = models.ForeignKey('Country', on_delete=models.CASCADE, )
    is_active = models.BooleanField('Actif', default=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    def __unicode__(self):
        return u'%s - %s' % (self.name.capitalize(), self.code.upper())

    class Meta:
        ordering = ["name"]

    # @classmethod
    # def create(cls, name,code):
    #     currency = cls(name=name.capitalize(), code=code.capitalize)
    #     # do something with the book
    #     return book

    def save(self, *args, **kwargs):
        #log.journalisation(self, cr, uid, vals, method='CREATION - juridiction_infraction')
        #raise ValueError(('Users must have an email address %s'),self)
        return super(Currency, self).save(*args, **kwargs)

class Profil(models.Model):
    """Model for profil with friendlist and comments"""
    user = models.OneToOneField(User, primary_key = True)  # La liaison OneToOne vers le modèle User
    #birthday = models.DateField(verbose_name='date de naissance', null=True, blank=True)
    SEXE_CHOICES = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autre'),
    )
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default='H')
    country_id = models.ForeignKey('credata.Country',blank=True,)
    tel = models.CharField(u'Téléphone', max_length=12, blank=False, help_text=u'Votre numéro de téléphone sans préfixe pays')
    is_custumer = models.BooleanField('Client', default=False,help_text=u'Cochez pour un client')
    image = models.ImageField(null=True, blank=True, upload_to="static/profil/%Y/%m/%d"
            , default='profil/defaultProfil.png')
    address = models.TextField(max_length=256, null=True, blank=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)
# friends = models.ManyToManyField('self', through = 'FriendList', 
    #       symmetrical = False, null=True, blank=True)

    def __unicode__(self):
        return "{0} {1}".format(self.user.last_name, self.user.first_name)

    def get_username(self):
        return str(self.user.last_name)+' '+ str(self.user.first_name)
    
    def get_full_name(self):
        return self.user.get_full_name()

    # def addFriend(self, friend_id):
    #     #user = Profil.
    #     return 0

class ContactUser(models.Model):
    """Model for profil with friendlist and comments"""
    name=models.CharField('Nom de famille', max_length=64, blank=False, )
    firstname=models.CharField(u'Prénoms', max_length=64, blank=False)
    SEXE_CHOICES = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autre'),
    )
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default='H')
    profil = models.ForeignKey(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    country_id = models.ForeignKey('credata.Country',blank=True,)
    tel = models.CharField(u'Téléphone', max_length=12, blank=False, help_text=u'Votre numéro de téléphone sans préfixe pays')
    is_active = models.BooleanField('Actif', default=True,help_text=u'Cochez pour activer ou désactiver')
    #is_custumer = models.BooleanField('Client', default=False,help_text=u'Cochez pour un client')
    address = models.TextField(max_length=256, null=True, blank=True)
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)


# class Order(models.Model):
#     name = models.CharField(u'Commande Numéro', max_length=24, help_text=u'Numéro de la commande.')
#     custumer_id = models.ForeignKey(User, on_delete=models.CASCADE, )
#     tel_source = models.CharField(u'Téléphone source', max_length=12, blank=False, help_text=u'Votre numéro de téléphone')
#     country_source  = models.ManyToManyField(Country, blank=True)
    
#     #contact = models.ForeignKey(CustumerContact, on_delete=models.CASCADE, blank=True, )
#     country_destination = models.ForeignKey('Country', on_delete=models.CASCADE, )
#     tel_destination = models.CharField(u'Téléphone destination', max_length=12, blank=False, help_text=u'Votre numéro de téléphone')
#     curruncy_destination = models.ForeignKey('Currency', on_delete=models.CASCADE, )
#     operator_destination = models.ForeignKey('Operator', on_delete=models.CASCADE, )

#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE, )
#     base_amount = models.DecimalField(u"Prix reçu par le destinataire", max_digits=6, decimal_places=0, blank=False, default=00)
#     currency_rate =  models.DecimalField(u"Taux de convertion", max_digits=8, decimal_places=5, blank=False, default=00)
#     currency_amount = models.DecimalField(u"Prix total en devise", max_digits=6, decimal_places=0, blank=False, default=00)
    
#     create_date = models.DateTimeField('Date de creation', auto_now_add=True)
#     update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    # def __unicode__(self):
    #     return u'%s ' % (self.name.capitalize())

    # class Meta:
    #     ordering = ["name"]

class Task(models.Model):
    order_id = models.CharField(u'id order', max_length=10, help_text='')
    operator_id = models.CharField('code ussd', max_length=10, help_text='')
    country_id = models.CharField('Country code', max_length=10, help_text='')
    list_state = (
        ('0', u'En traitement'),
        ('1', u'Complete'),
        ('2', u'Echouer'),
    )

    state = models.CharField('Type Ussd', choices=list_state, max_length=30, default='0')
    create_date = models.DateTimeField('Date de creation', auto_now_add=True)
    update_date = models.DateTimeField('Date de modification', auto_now=True)

    # create_uid=
    # update_uid=

    def __unicode__(self):
        return self.order_id

    class Meta:
        ordering = ["-order_id", 'country_id']




