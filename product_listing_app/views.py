from dataclasses import field
from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from product_listing_app.forms import FormPosts

from user_management_app.models import Profile
from .models import Post
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import ListView, DetailView, TemplateView, CreateView

# Create your views here.

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create_posts.html'
    fields = ['title', 'category', 'price', 'keywords', 'description', 'status', 'image']
    success_url = '/'
    
class ListPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name='posting'

    def get_queryset(self):
        return super().get_queryset()
