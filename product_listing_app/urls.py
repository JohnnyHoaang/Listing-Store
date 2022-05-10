from django.urls import path
from . import views
#from views import ListPosts, CreatePost

urlpatterns = [
    path ('',views.ListPosts.as_view(), name='posts'),
    path ('create/', views.CreatePost.as_view(), name='create'),
]
