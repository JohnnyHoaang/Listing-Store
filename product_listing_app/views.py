from .models import Post, Comment
from .forms import CreatePostForm, PostEditForm, PostCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

# Create your views here.
def LikedPostView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

class CreatePost(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'create_posts.html'
    # fields = ['title', 'author', 'category', 'price', 'keywords', 'description', 'status', 'image']
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
    # fields = ['title', 'author','category', 'price', 'keywords', 'description', 'status', 'image']
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

    def valid_form(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().valid_form(form)
