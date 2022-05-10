import datetime
from django.utils import timezone
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here:
class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    has_unread = models.BooleanField(default=False)

class Message(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    reciever_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    body = models.CharField(max_length=1000, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)