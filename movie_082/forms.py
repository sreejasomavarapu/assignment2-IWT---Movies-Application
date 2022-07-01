from dataclasses import fields
from django import forms
from . models import Movie
class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['rating']

