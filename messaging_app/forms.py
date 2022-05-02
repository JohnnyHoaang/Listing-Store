from django import forms
from .models import ThreadModel

class ThreadForm(forms.Form):
    usename = forms.CharField(label='', max_length=100)