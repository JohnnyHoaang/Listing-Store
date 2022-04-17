from tkinter import CASCADE
from django.db import models
from django import forms

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    def create_user(self, username, fname, lname, email, pwd):
        self.username = username
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.password = pwd