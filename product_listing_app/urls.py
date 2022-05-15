from django.urls import path
from requests import request
from .import views
from .views import CreatePost, PostDetailView, PostView, EditPostView, PostDeleteView, LikedPostView, CreateCommentView, RatingView, post
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path ('posts/',PostView.as_view(), name="posts"),
    #path ('create/', login_required(CreatePost.as_view(),login_url='/login'), name='create'),
    path ('create/', views.post, name='create'),
    path ('details/<int:pk>', login_required(PostDetailView.as_view(), login_url='/login'), name='details'),
    path ('details/<int:pk>/edit/', EditPostView.as_view(), name='edit'),
    path ('details/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path ('likes/<int:pk>', views.LikedPostView, name='post_likes'),
    path ('details/<int:pk>/comments/', CreateCommentView.as_view(), name='comments'),
    path ('details/<int:pk>/rating/', RatingView.as_view(), name='rating'),
]
