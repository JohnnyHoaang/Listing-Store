from django.urls import path
from . import views

urlpatterns = [
    path ('',views.ListPosts.as_view(), name='posts'),
    path ('create/', views.CreatePost.as_view(), name='create'),
    # path ('ratings/', )
    # path('create/', views.CreatePost.as_view(), name='create'),
    # path('details', views.DetailedPost.as_view(), name='detailed_post')
]
