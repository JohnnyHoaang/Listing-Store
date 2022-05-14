from django import forms
from django.contrib.auth.models import User

from product_listing_app.models import Post


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'price', 'keywords', 'status']

class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups']
