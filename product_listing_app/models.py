from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=2000)
    #maybe a dropdown here?
    post_category = models.CharField(max_length=2000, default="Books")
    # post_price = 
    # post_keywords = 
    post_description = models.CharField(max_length=2000)
    #maybe a drop down for this?
    post_status = models.CharField(max_length=2000, default="status")
    #post_image = 
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        post_value = f'Title: {self.post_title} \n Category: {self.post_category}'
        return f'{post_value}'
