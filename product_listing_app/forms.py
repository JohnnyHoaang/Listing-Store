from django import forms
from datetime import datetime, date

from product_listing_app.models import Post

class FormPosts(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    creation_date = forms.DateField()

    def clean_due_date(self):
        data = self.cleaned_data['creation_date']
        #Validation
        if data < date.today():
            raise forms.ValidationError("Invalid due date")
        return data