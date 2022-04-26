from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/members', views.index, name='members'),
    path('dashboard/admin_users',views.admin_manage_users, name='admin_users'),
    path('dashboard/json', views.json, name='json')
]