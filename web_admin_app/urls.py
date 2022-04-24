from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/members', views.index, name='members'),
]