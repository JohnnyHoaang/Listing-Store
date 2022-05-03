from django import forms
from .models import ThreadModel

class ThreadForm(forms.Form):
    usename = forms.CharField(label='', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)