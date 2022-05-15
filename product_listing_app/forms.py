from django import forms
from datetime import datetime, date
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title', 'author', 'category', 'price', 'keywords', 'description', 'status', 'image']
       widgets = {
            'title': forms.TextInput(attrs={'class':'form-styling'}),
            'author': forms.TextInput(attrs={'class':'form-styling', 'value':'', 'id':'username', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-styling'}),
            'category': forms.Select(attrs={'class':'form-styling'}),
            'price': forms.NumberInput(attrs={'class':'form-styling'}),
            'keywords': forms.TextInput(attrs={'class':'form-styling'}),
            'description': forms.Textarea(attrs={'class':'form-styling'}),
            'status': forms.Select(attrs={'class':'form-styling'}),
            'image': forms.FileInput(attrs={'class':'form-styling'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['title', 'author', 'category', 'price', 'keywords', 'description', 'status', 'image']
       widgets = {
            'title': forms.TextInput(attrs={'class':'form-styling'}),
            'author': forms.TextInput(attrs={'class':'form-styling'}),
            #'author': forms.Select(attrs={'class':'form-styling'}),
            'category': forms.Select(attrs={'class':'form-styling'}),
            'price': forms.NumberInput(attrs={'class':'form-styling'}),
            'keywords': forms.TextInput(attrs={'class':'form-styling'}),
            'description': forms.Textarea(attrs={'class':'form-styling'}),
            'status': forms.Select(attrs={'class':'form-styling'}),
            'image': forms.FileInput(attrs={'class':'form-styling'}),
        }

class PostCommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ['commenter', 'text']
       widgets = {
            'commenter': forms.TextInput(attrs={'class':'form-styling'}),
            'text': forms.Textarea(attrs={'class':'form-styling'}),
        }