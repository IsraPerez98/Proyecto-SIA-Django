from django import forms
#from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from allauth.socialaccount.forms import SignupForm
from allauth.account.adapter import DefaultAccountAdapter
from .models import Usuario

import re

#solo emails de utem.cl
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@utem.cl$)"

class MyAdapter(DefaultAccountAdapter):

    def clean_email(self,email):
        email = super().clean_email(email)

        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError('Solo se permiten correos de @utem.cl')

        return email

class RegistroForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('username','email')


class CambiarUsuarioForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'email')