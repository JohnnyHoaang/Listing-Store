from django.urls import path
from .views import ListPost, CreatePost

urlpatterns = [
    path ('',ListPost.as_view(), name='posts'),
    path ('create/', CreatePost.as_view(), name='create'),
]
