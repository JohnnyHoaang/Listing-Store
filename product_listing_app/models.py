from django.db import models

# Create your models here.
class Post(models.Model):
    books = 'Books'
    cd = 'CDs'
    videos = 'Videos'
    movies = 'Movies'
    tv_show = 'TV Shows'
    categories_for_posts = [
        (books,'Books'),
        (cd, 'CDs'),
        (videos, 'Videos'),
        (movies, 'Movies'),
        (tv_show, 'TV Shows'),
    ]
    pg_13 = 'PG13'
    status_r = 'R'
    pg = 'PG'
    explicit = 'Explicit'
    status_for_posts = [
        (pg_13, 'PG13'),
        (status_r, 'R'),
        (pg, 'PG'),
        (explicit, 'Explicit'),
    ]
    post_title = models.CharField(max_length=2000)
    post_category = models.CharField(max_length=2000, choices=categories_for_posts, default=books)
    # post_price = 
    # post_keywords = 
    post_description = models.CharField(max_length=2000)
    post_status = models.CharField(max_length=2000, choices=status_for_posts, default=pg_13)
    #post_image = 
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        post_value = f'Title: {self.post_title} \n Category: {self.post_category}'
        return f'{post_value}'
