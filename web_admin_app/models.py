from django.db import models
from user_management_app.models import Account
# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=100)
    account = models.ManyToManyField(Account, through='PersonGroup', through_fields=('group', 'account'))
    def __str__(self):
        return self.group_name
class PersonGroup(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.account}'

