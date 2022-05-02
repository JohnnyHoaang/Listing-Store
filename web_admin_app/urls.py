from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/members', views.members_page, name='members'),
    path('dashboard/admin_users',views.admin_manage_users, name='admin_users'),
    path('dashboard/admin_items', views.admin_manage_items, name='admin_items'),
    path('dashboard/admin_delete_user/<str:username>' , views.delete_user, name='delete_users_ai'),
    path('dashboard/admin_delete_user/<str:username>' , views.delete_user, name='delete_users_au'),
    path('dashboard/admin_delete_post/<str:post_title>' , views.delete_post, name='delete_posts'),
]