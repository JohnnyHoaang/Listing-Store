from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create_posts.html'
    fields = ['title', 'author', 'category', 'price', 'keywords', 'description', 'status', 'image']
    success_url = '/posts/'
    
class PostView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name= 'posts'
    ordering = ['-date']
    #encoded_image = base64.b64encode(request.user.profile.avatar).decode("utf-8")

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class EditPostView(UpdateView):
    model = Post
    template_name = 'editing_posts.html'
    fields = ['title', 'author', 'category', 'price', 'keywords', 'description', 'status', 'image']
    success_url = '/posts/'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'deleting_posts.html'
    success_url = '/posts/'