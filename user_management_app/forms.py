from django import forms

class CreateUserForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.PasswordInput(widget=forms.PasswordInput())
