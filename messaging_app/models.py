from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    value = models.CharField(max_length=1000000)