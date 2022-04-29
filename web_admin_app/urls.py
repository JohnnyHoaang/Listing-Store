from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/members', views.members_page, name='members'),
    path('dashboard/admin_users',views.admin_manage_users, name='admin_users'),
]