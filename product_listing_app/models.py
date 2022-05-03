from django.db import models

# Create your models here.
class Post(models.Model):
    categories_for_posts = [
        ('Books','Books'),
        ('CDs','CDs'),
        ('Videos','Videos'),
        ('Movies','Movies'),
        ('TV Shows','TV Shows'),
    ]
    status_for_posts = [
        ('PG13','PG13'),
        ('R','R'),
        ('PG','PG'),
        ('Explicit', 'Explicit'),
    ]
    title = models.CharField(max_length=2000)
    category = models.CharField(max_length=2000, choices=categories_for_posts, default=categories_for_posts)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    keywords = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2000, choices=status_for_posts, default=status_for_posts)
    image = models.ImageField(upload_to='', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        post_value = f'Title: {self.title}'
        return f'{post_value}'
