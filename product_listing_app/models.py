from django.db import models

# Create your models here.
'''
class Post(models.Model):
    post_title = models.CharField(max_length=2000)
    post_description = models.CharField(max_length=2000)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_title} {self.post_description} ({self.post_date})'
'''