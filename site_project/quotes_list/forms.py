from django import forms
from . import models
from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Authors, Quotes, Tag

class CreateQuoteForm(ModelForm):
    author = forms.ModelChoiceField(queryset = Authors.objects.values_list("fullname"), widget=forms.Select(attrs={'class':'dropdown'}))
    quote = forms.CharField(max_length=1000, required=True, widget=forms.TextInput())


    class Meta:
        model = Quotes
        fields = ["quote", "author"]
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
    name = forms.CharField(min_length=3, max_length=25, required=True, widget=forms.TextInput())

    class Meta:
        model = Tag
        fields = ['name']
