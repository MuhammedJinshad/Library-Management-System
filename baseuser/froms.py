from django import forms
from django.contrib.auth.forms import UserCreationForm

from baseuser.models import Account 


class RegistrationFrom(UserCreationForm):
    email   =   forms.EmailField(max_length=60, help_text='Required. Add a valid email address ')

    class Meta:
        Modul   =   Account
        field   =   ("email","username","password1","password2")