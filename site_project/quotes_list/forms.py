from django import forms
from . import models
from django.forms import ModelForm
from .models import Authors, Quotes

class CreateQuoteForm(ModelForm):
    author = forms.ChoiceField(choices=models.Authors.fullname)
    quote = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    class Meta:
        model = models.Quotes
        fields = ["author", "quote"]
        exclude = ['tags']


class CreateAuthorForm(ModelForm):
    fullname = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    born_date = forms.DateField(max_length=100, required=True, widget=forms.DateInput())
    born_location = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    description = forms.CharField(max_length=1000, required=True, widget=forms.TextInput())

    class Meta:
        model = models.Quotes
        fields = ["fullname", "born date", "born location", "description"]