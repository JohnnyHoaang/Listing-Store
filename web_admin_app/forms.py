from django import forms
from django.contrib.auth.models import User

from product_listing_app.models import Post


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'category', 'price', 'keywords', 'status', 'image']

class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups']
