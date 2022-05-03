from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.template import loader

from django.views.generic import ListView, DetailView, TemplateView, CreateView

# Create your views here.
class ListPosts(ListView):
    posts = Post.objects.filter(post_status=1).order_by('-post_date')
    template_name = 'posts.html'

class DetailedPost(DetailView):
    model = Post
    template_name = 'posts.html'


class CreatePost(CreateView):
    form_class = Post
    template_name = 'create_posts.html'
    success_url = 'create/'
    '''
    def valid_form(self, post):
        post
    
    '''

def homepage(request):
    return render(request, "posts.html")


def display_post(request):
    display_post = Post.objects.get()
    template = loader.get_template('user_management_app/base.html')
    context = {
        'display_post': display_post,
    }

    return HttpResponse(template.render(context, request))

def user_post(self):
        # user = get_user(self.request).user
        # if user.is_authenticated():
        pass

def create_post(request):
    #return redirect("create_posts.html")
    creating = Post.objects.get()
    template = loader.get_template('create_posts.html')
    context = {
        'creating' : creating,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, "create_posts.html")
    

'''
def add_post(request):
    title = None
    if request.method == 'POST':
        title = request.POST.get('post_title', None)
        template = loader.get_template('todo_app/base.html')
        context = {
            'title' : title
        }
    return HttpResponse(template.render(context, request))
    '''

