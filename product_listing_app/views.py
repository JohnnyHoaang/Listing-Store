from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template import loader

# Create your views here.
def index(request):
    post = Post.objects.order_by('-title')[:5]
    template = loader.get_template('product_listing_app/product_posts.html')
    context = {
        'prod_posts': post,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'product_posts.html')
'''
def create_post(request):
    prod_posts = Posts.objects.get(prod_posts=prod_posts)
    template = loader.get_template('product_listing_app/product_posts.html')
    context = {
        'prod_posts': prod_posts,
    }

    return HttpResponse(template.render(context, request))
'''
