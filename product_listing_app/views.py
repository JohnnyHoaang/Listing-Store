from dataclasses import field
from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from product_listing_app.forms import FormPosts

from user_management_app.models import Profile
from .models import Post
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import ListView, DetailView, TemplateView, CreateView

# Create your views here.
class ListPosts(ListView):
    posts = Post.objects.filter(status=1).order_by('-date')
    template_name = 'posts.html'

class DetailedPost(DetailView):
    model = Post
    template_name = 'posts.html'


class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create_posts.html'
    success_url = 'create/'
    fields = ['title', 'category', 'price', 'keywords', 'description', 'status', 'image']

    def valid_form(self):
        pass
    

def homepage(request):
    return render(request, "posts.html")

def display_posts(request):
    if request.method == 'POST':
        form_post = FormPosts(request.POST)
        if form_post.is_valid():
            form_post.instance.user = request.user
            form_post.save()
            messages.success(request, 'Your post was successfully created!')
            return redirect('login')
        else:
            messages.error(request, 'There was an error!')
    else:
        post_form = FormPosts()
        context = {
            'post_form': post_form
        }
        return render(request, "posts.html", context)

'''
def display_post(request):
    display_post = Post.objects.get()
    template = loader.get_template('user_management_app/base.html')
    context = {
        'display_post': display_post,
    }

    return HttpResponse(template.render(context, request))
'''
'''
def post_image(request):
    #encoded = b64encode(model.image).decode('ascii')
    #render_to_string ('lib / forms / imageform.html', {"image": encoded}, request)
    myImage = request.FILES['myRow'].file.read()
'''