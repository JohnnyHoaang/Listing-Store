import base64
from .models import Post, Comment, Rating
from .forms import CreatePostForm, PostEditForm, PostCommentForm, RatingForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def LikedPostView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

def post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.FILES.get('image', False):
                img = request.FILES['image'].file.read()
                post.image=img
                post.save()
            return redirect('/posts/')
    else:
        form = CreatePostForm()
    context = {
        'form':form,
    }
    return render(request, "create_posts.html", context)

    
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
'''
class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'editing_posts.html'
    success_url = '/posts/'
'''
def edit_post(request, pk):
    posting = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostEditForm(data=request.POST, instance=posting)
        if request.FILES.get('image', False):
             img = request.FILES['image'].file.read()
             Post.objects.filter(id=pk).update(image=img)
        if form.is_valid():
            post = form.save(commit=False)
            img = post.image
            #Post.objects.filter(id=pk).update(title=post.title, category=post.category, price=post.price, keywords=post.keywords, description=post.description, status=post.status)
            form.save()
        return redirect('/posts/')
    else:
        form = PostEditForm(instance=posting)
    context = {
        'post':posting,
        'form':form,
    }
    return render(request, 'editing_posts.html', context)

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