from typing import List
from django.urls import path
from . import views
from .views import CreateThread, ListTreads

urlpatterns = [
    path('messaging', views.home, name='message'),
    path('inbox/', ListTreads.as_view(), name='inbox'), 
    path('inbox/create-thread', ListTreads.as_view(), name='create-thread')
]