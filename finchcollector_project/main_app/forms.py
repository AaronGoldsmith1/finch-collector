from django import forms
from .models import Finch, Feeding


class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = ['name', 'species', 'description', 'age']


class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
