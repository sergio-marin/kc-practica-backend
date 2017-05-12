from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=False, help_text='Optional.')
    last_name = forms.CharField(required=False, help_text='Optional.')
    email = forms.EmailField(help_text='Required.')

    class Meta:
            model = User
            fields = ["username", "first_name", "last_name", "email"]
