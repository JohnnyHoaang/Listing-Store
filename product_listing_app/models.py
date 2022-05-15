import base64
from tkinter import CASCADE
from django.db import models
#from djangoratings.fields import RatingField
from django.urls import reverse
from star_ratings.models import Rating
from product_listing_project import settings
from user_management_app.models import User

# Create your models here.
class Post(models.Model):
    categories_for_post = [
        ('Books','Books'),
        ('CDs','CDs'),
        ('Videos','Videos'),
        ('Movies','Movies'),
        ('TV Shows','TV Shows'),
        ('Other', 'Other')
    ]
    status_for_post = [
        ('PG13','PG13'),
        ('R','R'),
        ('PG','PG'),
        ('Explicit', 'Explicit'),
        ('Other', 'Other')
    ]
    title = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=2000, choices=categories_for_post, default=categories_for_post)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    keywords = models.CharField(max_length=2000, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2000, choices=status_for_post, default=status_for_post)
    image = models.BinaryField(blank=True, null=True, editable=True)
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    flagged = models.BooleanField(default=False)

    def __str__(self):
        post_value = f'Title: {self.title}'
        return f'{post_value}'

    @property
    def convert_image(self):
        encode_image = base64.b64encode(self.image).decode('utf-8')
        return encode_image
    
    def get_absolute_url(self):
        return reverse('posts/')

    def get_count_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="comment")
    text = models.TextField(blank=True, null=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('posts/')

class Rating(models.Model):
    rating_for_posts = [
        (0,'0'),
        (1,'1'),
        (2,'2'), 
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    posting = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="rated")
    rater = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
    rate = models.PositiveSmallIntegerField(blank=True, null=True,choices=rating_for_posts)

    def __str__(self):
        return self.comment