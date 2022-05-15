import base64
from .models import Post, Comment, Rating
from .forms import CreatePostForm, PostEditForm, PostCommentForm, RatingForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def LikedPostView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

class CreatePost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_posts.html'
    success_url = '/posts/'
    '''
    def post(self, request, post_id):
        encoded_image = None
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                if request.FILES.get('image', False):
                    image = request.FILES['image'].file.read()
                    return redirect('/posts/')
        else:
            form = CreatePostForm()
        context = {
            'form':form,
            'encoded_image':encoded_image,
        }
        return render(request, self.template_name, context)
    '''
    '''
    def get(self, request):
        value = 
        return render(request, self.template_name, {"value":value})
'''
class PostView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name= 'posts'
    ordering = ['-date']
    success_url = '/'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        query = get_object_or_404(Post, id=self.kwargs['pk'])
        like_count = query.get_count_likes()
        context["like_count"] = like_count
        return context

class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'editing_posts.html'
    success_url = '/posts/'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'deleting_posts.html'
    success_url = '/posts/'

class CreateCommentView(CreateView):
    model = Comment
    form_class = PostCommentForm
    template_name = 'create_comment.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class RatingView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'rating_posts.html'
    success_url = '/posts/'