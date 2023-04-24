from django import forms
from . import models
from django.forms import ModelForm
from .models import Authors, Quotes, Tag

class CreateQuoteForm(ModelForm):
    author = forms.ChoiceField(choices=models.Authors.objects.all())
    quote = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    class Meta:
        model = Quotes
        fields = ["author", "quote"]
        exclude = ['tags']


class CreateAuthorForm(ModelForm):
    fullname = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    born_date = forms.DateField(required=True, widget=forms.DateInput())
    born_location = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    description = forms.CharField(max_length=1000, required=True, widget=forms.TextInput())

    class Meta:
        model = Authors
        fields = ["fullname", "born_date", "born_location", "description"]


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']
