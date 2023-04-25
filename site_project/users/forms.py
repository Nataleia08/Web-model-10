from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    email = forms.CharField(max_length=150,
                                required=False,
                                widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100,required=False,widget=forms.TextInput())
    last_name = forms.CharField(max_length=100,required=False,widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']