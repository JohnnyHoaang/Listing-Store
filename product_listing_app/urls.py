from django.urls import path
from .views import CreatePost, PostView

urlpatterns = [
    path ('posts/',PostView.as_view(), name="posts"),
    path ('create/', CreatePost.as_view(), name='create'),
]
