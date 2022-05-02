from typing import List
from django.urls import path
from . import views
from .views import CreateThread, ListTreads, ThreadView, CreateMessage

urlpatterns = [
    path('', views.home, name='message'),
    path('inbox/', ListTreads.as_view(), name='inbox'), 
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message')
]