from django.urls import path
from . import views

urlpatterns = [
    path('messaging', views.home, name='message')
]