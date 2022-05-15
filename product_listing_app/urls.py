from django.urls import path
from .views import CreatePost, PostDetailView, PostView, EditPostView, PostDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path ('posts/',PostView.as_view(), name="posts"),
    path ('create/', CreatePost.as_view(), name='create'),
    path ('details/<int:pk>', login_required(PostDetailView.as_view(), login_url='/login'), name='details'),
    path ('details/<int:pk>/edit/', EditPostView.as_view(), name='edit'),
    path ('details/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
