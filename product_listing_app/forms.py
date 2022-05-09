from django import forms

from product_listing_app.models import Post

class FormPosts(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'price', 'keywords', 'description', 'status', 'image']