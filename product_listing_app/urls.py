from django.urls import path
from . import views
from .views import CreateCommentView, CreatePost, PostDetailView, PostView, EditPostView, PostDeleteView, LikedPostView, RatingView

urlpatterns = [
    path ('posts/',PostView.as_view(), name="posts"),
    path ('create/', CreatePost.as_view(), name='create'),
    path ('details/<int:pk>', PostDetailView.as_view(), name='details'),
    path ('details/<int:pk>/edit/', EditPostView.as_view(), name='edit'),
    path ('details/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path ('likes/<int:pk>', views.LikedPostView, name='post_likes'),
    path ('details/<int:pk>/comments/', CreateCommentView.as_view(), name='comments'),
    path ('details/<int:pk>/rating/', RatingView.as_view(), name='rating'),
]
