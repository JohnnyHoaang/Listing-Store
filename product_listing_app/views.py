import base64
from django.template import loader
from .models import Post, Comment, Rating, AzureImage, MyImage
from .forms import CreatePostForm, PostEditForm, PostCommentForm, RatingForm, MyImageForm
from django.http import HttpResponse, HttpResponseRedirect
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

class PostView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name= 'posts'
    ordering = ['-date']
    success_url = '/'
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

def display_image(request, image_id):   
    image = AzureImage.objects.get(id=image_id)
    template = loader.get_template('view_image.html')
    context = {
        'image_url': image.image.url,
    }
    return HttpResponse(template.render(context, request))

def add_my_image(request):
    form = None
    if request.method == 'POST':
        form = MyImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Add to the database
            image_file = form.cleaned_data['image']
            from product_listing_app.image_utils import image_to_binary
            byte_arr = image_to_binary(image_file)
            item = MyImage(image=byte_arr)
            item.save()
            return HttpResponseRedirect(redirect_to=reverse('display-image', kwargs={'image_id':item.id}))
    else:
        form = MyImageForm()
    template = loader.get_template('todo_app/image_upload.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))
