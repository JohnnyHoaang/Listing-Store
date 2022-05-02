from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('home/create', views.create_post, name='create_post'),
]
