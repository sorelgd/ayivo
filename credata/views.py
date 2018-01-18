# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, render_to_response
from .forms import ConnexionForm
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Country,Product,Category,CodeUssd,OperatorPrefixe,Operator,Currency,Profil,ContactUser
from django.contrib.auth.models import User
from datetime import datetime
from random import choice
from string import letters
from django.forms.formsets import formset_factory
from django.template import RequestContext

#from credata.forms import SignInForm, SignUpForm, ProfilForm
# Create your views here.

def index(request):
    queryset = Country.objects.filter(is_active=True, is_couvrage=True).order_by('name')
    current_user = request.user
    context = {
        "country": queryset,
        "user":current_user,
    }
    return render(request, "credata/index.html", context)

def profiluser(request):
    current_user = request.user
    context = {
        "user":current_user,
    }
    return render(request, "credata/profiluser.html", context)

def credits(request):
    cat = Category.objects.filter(code='crd').order_by('name')
    queryset = Product.objects.filter(is_active=True, category_id=cat).order_by('id')
    current_user = request.user
    context = {
        "credit": queryset,
        "user":current_user,
    }
    return render(request, "credata/credits.html", context)

def datas(request):
    cat = Category.objects.filter(code='dat').order_by('name')
    queryset = Product.objects.filter(is_active=True, category_id=cat).order_by('id')
    current_user = request.user
    context = {
        "datas": queryset,
        "user":current_user,
    }
    return render(request, "credata/datas.html", context)

def moneys(request):
    cat = Category.objects.filter(code='mon').order_by('name')
    queryset = Product.objects.filter(is_active=True, category_id=cat).order_by('id')
    current_user = request.user
    context = {
        "moneys": queryset,
        "user":current_user,
    }
    return render(request, "credata/moneys.html", context) 

def contactsuser(request):

    current_user = request.user
    compl= ContactUser.objects.all().filter(profil=current_user.id)

    len_hist=[1,2,3]
    context = {
        #"moneys": queryset,
        "len":compl,
        "user":current_user,
    }
    return render(request, "credata/contacts.html", context)

def historiquesuser(request):
    #cat = Category.objects.filter(code='mon').order_by('name')
    #queryset = Product.objects.filter(is_active=True, category_id=cat).order_by('id')
    len_hist=[1,2,3]
    current_user = request.user
    context = {
        #"moneys": queryset,
        "user":current_user,
        "len":len_hist
    }
    return render(request, "credata/historiques.html", context)

def infospersonel(request):
    current_user = request.user
    usr=current_user.id
    compl= Profil.objects.all().filter(user=usr)[0]

    context = {
        #"moneys": queryset,
        "user":current_user,
        "profil":compl
    }
    return render(request, "credata/infospersonel.html", context)

def faireunachat(request):
    #cat = Category.objects.filter(code='mon').order_by('name')
    #queryset = Product.objects.filter(is_active=True, category_id=cat).order_by('id')
    len_hist=[1,2,3]
    current_user = request.user
    context = {
        #"moneys": queryset,
        "user":current_user,
        "len":len_hist
    }
    return render(request, "credata/faireunachat.html", context)


def deconnexion(request):
    logout(request)
    return redirect(login)

# def sign_up(request):
#     """ User sign up form """
#     if request.method == 'POST':
# #        data = request.POST.copy() # so we can manipulate data

#         # random username
#  #       data['username'] = ''.join([choice(letters) for i in xrange(30)])
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             user = form.save()
# #            return HttpResponseRedirect('login/login.html')
#             return HttpResponseRedirect(reverse("wifttbook:profil"))
#     else:
#         form = SignUpForm()

#     return render_to_response('credata/comptewiftt.html', {'form':form},
#                               context_instance=RequestContext(request))

# def sign_in(request):
#     error = False

#     if request.method == "POST":
#         form = SignInForm(request.POST)

#         if form.is_valid():
#             email = form.cleaned_data["email"]  # Nous récupérons l'adresse electronique
#             password = form.cleaned_data["password"]  # … et le mot de passe
#             user = authenticate(username=email, password=password)  #Nous vérifions si les données sont correctes
#             if user:  # Si l'objet renvoyé n'est pas None
#                 login(request, user)  # nous connectons l'utilisateur
#             else: #sinon une erreur sera affichée
#                 error = True

#     else:
#         form = SignInForm()
#     context={'form':form}
#     return render(request,"credata/connexion.html", context)


