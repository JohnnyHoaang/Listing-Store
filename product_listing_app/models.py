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
    ]
    status_for_post = [
        ('PG13','PG13'),
        ('R','R'),
        ('PG','PG'),
        ('Explicit', 'Explicit'),
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
    #user_likes = models.ManyToManyField(User)
    #rating = RatingField(range=5, can_change_vote = True, allow_anonymous = False)
    #rating  = GenericRelation(Rating, related_query_name='posts')

    def __str__(self):
        post_value = f'Title: {self.title}'
        return f'{post_value}'

    @property
    def convert_image(self):
        # or decode('ascii')
        encode_image = base64.b64encode(self.image).decode('utf-8')
        return encode_image
    
    def get_absolute_url(self):
        return reverse('posts/')