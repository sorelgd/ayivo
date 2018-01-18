from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from credata.models import Profil, Country

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SignInForm(forms.Form):
    """Sign In with email and password"""
    email = forms.EmailField(label='Adresse electronique', max_length=75)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    """ Require email address when a user signs up """
    # a username birthday and sexe fields and profil photo
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.PasswordInput)
    country_id = forms.DateField(label='Pays', required=True)#, widget=SelectDateWidget(years = range(datetime.now().year - 7, 1949, -1)))
    sexe = forms.ChoiceField(label='Sexe', choices=Profil.SEXE_CHOICES)
    image = forms.ImageField(label='Photo de profil', required=False)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists. Did you forget your password?")
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        email = self.cleaned_data["email"]
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
#        user.first_name = self.cleaned_data["first_name"]
#        user.last_name = self.cleaned_data["last_name"]
        user.is_active = True # change to false if using email activation
        if commit:
            user.save()
 #           birthday = self.cleaned_data["birthday"]
 #           sexe = self.cleaned_data["sexe"]
  #          image = self.cleaned_data["image"]
            p = Profil(user=user, country_id=None, sexe=None, image=None)
            p.save()
        return user

class ProfilForm(ModelForm):

    class Meta:
        model = Profil
        fields = '__all__' #('username', 'last_name', 'first_name', 'birthday', 'sexe', 'email')

