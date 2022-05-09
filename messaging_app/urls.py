from typing import List
from django.urls import path
from . import views
from .views import CreateThread, ListThreads, ThreadView, CreateMessage

urlpatterns = [
    path('', views.home, name='message'),
    path('inbox/', views.ListThreads.as_view(), name='inbox'), 
    path('inbox/create-thread/', views.CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>', views.ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', views.CreateMessage.as_view(), name='create-message')
]