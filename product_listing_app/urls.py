from django.urls import path
from . import views

urlpatterns = [
    #path('home', views.homepage, name='home'),
    #path('home/create', views.create_post, name='create_post'),
    path ('',views.ListPosts.as_view(), name='posts'),
    path('details', views.DetailedPost.as_view(), name='detailed_post')
]
