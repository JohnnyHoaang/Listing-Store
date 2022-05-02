from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template import loader

from django.views.generic import ListView, DetailView

# Create your views here.
class ListPosts(ListView):
    posts = Post.objects.filter(status=1).order_by('-post_date')
    template_name = 'homepage.html'

class DetailedPost(DetailView):
    model = Post
    template_name = 'posts.html'


def homepage(request):
    return render(request, "homepage.html")

def create_post(request):
    create_post = Post.objects.get()
    template = loader.get_template('product_listing_app/homepage.html')
    context = {
        'create_post': create_post,
    }

    return HttpResponse(template.render(context, request))

def add_post(request):
    title = None
    if request.method == 'POST':
        title = request.POST.get('post_title', None)
        template = loader.get_template('todo_app/homepage.html')
        context = {
            'title' : title
        }
    return HttpResponse(template.render(context, request))

