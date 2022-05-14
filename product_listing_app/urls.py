from django.urls import path
from .views import CreatePost, PostDetailView, PostView, EditPostView, PostDeleteView

urlpatterns = [
    path ('posts/',PostView.as_view(), name="posts"),
    path ('create/', CreatePost.as_view(), name='create'),
    path ('details/<int:pk>', PostDetailView.as_view(), name='details'),
    path ('details/<int:pk>/edit/', EditPostView.as_view(), name='edit'),
    path ('details/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
