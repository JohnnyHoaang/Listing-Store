from django import forms
from datetime import datetime, date
from .models import Post, Comment, Rating


class CreatePostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title', 'author', 'category', 'price', 'keywords', 'description', 'status', 'flagged','image']
       widgets = {
            'title': forms.TextInput(attrs={'class':'form-styling'}),
            'author': forms.TextInput(attrs={'class':'form-styling', 'value':'', 'id':'username', 'type':'hidden'}),
            'category': forms.Select(attrs={'class':'form-styling'}),
            'price': forms.NumberInput(attrs={'class':'form-styling'}),
            'keywords': forms.TextInput(attrs={'class':'form-styling'}),
            'description': forms.Textarea(attrs={'class':'form-styling'}),
            'status': forms.Select(attrs={'class':'form-styling'}),
            'flagged': forms.TextInput(attrs={'class':'form-styling'}),
            'image': forms.FileInput(attrs={'class':'form-styling','type':'hidden'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['title','category', 'price', 'keywords', 'description', 'status','flagged', 'image']
       widgets = {
            'title': forms.TextInput(attrs={'class':'form-styling'}),
            'category': forms.Select(attrs={'class':'form-styling'}),
            'price': forms.NumberInput(attrs={'class':'form-styling'}),
            'keywords': forms.TextInput(attrs={'class':'form-styling'}),
            'description': forms.Textarea(attrs={'class':'form-styling'}),
            'status': forms.Select(attrs={'class':'form-styling'}),
            'flagged': forms.TimeInput(attrs={'class':'form-styling'}),
            'image': forms.FileInput(attrs={'class':'form-styling', 'type':'hidden'}),
        }
    '''
    def update_post(self, title, category, price, keywords, description, status, flagged, image):
        self.title = title
        self.category = category
        self.price = price
        self.keywords = keywords
        self.description = description
        self.status = status
        self.flagged = flagged
        self.image = image
'''

class PostCommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ['post','commenter', 'text']
       widgets = {
            'post': forms.TextInput(attrs={'class':'form-styling', 'value':'','id':'post-title', 'type':'hidden'}),
            'commenter': forms.TextInput(attrs={'class':'form-styling', 'value':'', 'id':'commentee', 'type':'hidden'}),
            'text': forms.Textarea(attrs={'class':'form-styling'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['posting','rater','comment','rate']
        widgets = {
            'posting': forms.Select(attrs={'class':'form-styling', 'value':'','id':'posttitle'}),
            'rater': forms.TextInput(attrs={'class':'form-styling', 'value':'', 'id':'username-rate', 'type':'hidden'}),
            'comment': forms.Textarea(attrs={'class':'form-styling'}),
            'rate': forms.Select(attrs={'class':'form-styling'}),
        }