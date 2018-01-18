from django.contrib import admin
from .models import Country, Category, Product, Operator, CodeUssd, OperatorPrefixe, Currency, Task,Profil,ContactUser
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "indicatif", "is_active","is_couvrage")
    list_display_links = ('name', 'code')
    list_filter = ('name', 'code','indicatif','is_active','is_couvrage')

    class Meta:
        model = Country


admin.site.register(Country, CountryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "parent", "is_active")
    list_display_links = ('name', 'code')
    list_filter = ('name', 'code','parent','is_active')


    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "category_id", "price", "is_active")
    list_display_links = ('name', 'code')
    list_filter = ('price', 'code','category_id','is_active')


    class Meta:
        model = Product
    #A TESTER PAR LA SUITE
    # def clean_price(self):
    #     if self.cleaned_data['price'] <= 0:
    #         raise forms.ValidationError('Price must be greater than zero.')
    #     return self.cleaned_data['price']

admin.site.register(Product, ProductAdmin)


class OperatorAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "country_id", "is_active")
    list_display_links = ('name', 'code')
    list_filter = ('name', 'code','country_id','is_active')

    class Meta:
        model = Operator


admin.site.register(Operator, OperatorAdmin)


class CodeUssdAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "operator_id", "ussd_type", "is_active")
    list_display_links = ('name', 'code')
    list_filter = ('name', 'code','operator_id','is_active','ussd_type')
    #readonly_fields = ('operator_id',)

    class Meta:
        model = CodeUssd


admin.site.register(CodeUssd, CodeUssdAdmin)


class OperatorPrefixeAdmin(admin.ModelAdmin):
    list_display = ("name", "operator_id", "is_active")
    list_display_links = ('name', 'operator_id')
    list_filter = ('name', 'operator_id','is_active')

    class Meta:
        model = OperatorPrefixe

admin.site.register(OperatorPrefixe, OperatorPrefixeAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active")
    list_display_links = ('name', 'code')
    list_filter = ('name', 'code','countrys','is_active')

    class Meta:
        model = Currency

admin.site.register(Currency, CurrencyAdmin)


class ContactUserAdmin(admin.ModelAdmin):
    list_display = ("name", "firstname", "sexe", "country_id", "tel","profil","is_active")
    list_display_links = ('name', 'firstname')
    list_filter = ("name", "firstname", "sexe", "country_id", "tel","profil","is_active")

    class Meta:
        model = ContactUser
admin.site.register(ContactUser, ContactUserAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("order_id", "operator_id", "country_id")

    class Meta:
        model = Task
admin.site.register(Task, TaskAdmin)

class ProfilInline(admin.StackedInline):
    '''Define an inline admin descriptor for Profil model
    which acts a bit like a singleton
    '''
    model = Profil
    can_delete = False
    verbose_name_plural = 'Profil'

# Define a new User admin

class UserAdmin(UserAdmin):
    ''' Define a new User admin
    '''
    inlines = (ProfilInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
