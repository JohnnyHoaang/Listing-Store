from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/members', views.members_page, name='members'),
    path('dashboard/admin_users',views.admin_manage_users, name='admin_users'),
    path('dashboard/admin_items', views.admin_manage_items, name='admin_items'),
    path('dashboard/admin', views.admin_access, name='admin'),
    path('dashboard/admin_items/user/<str:username>' , views.delete_user_admin_items, name='delete_users_admin_items'),
    path('dashboard/admin_users/user/<str:username>' , views.delete_user_admin_users, name='delete_users_admin_users'),
    path('dashboard/admin_items/post/<str:title>' , views.delete_post, name='delete_posts'),
]