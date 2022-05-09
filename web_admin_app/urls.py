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
    path('dashboard/admin_users/add_member', views.add_member_users, name='add_member_users'),
    path('dashboard/admin_items/add_member', views.add_member_items, name='add_member_items'),
    path('dashboard/admin_users/block_member/<str:username>', views.block_member_admin_users, name ='block_member_users'),
    path('dashboard/admin_users/unblock_member/<str:username>', views.unblock_member_admin_users, name ='unblock_member_users'),
    path('dashboard/admin_items/block_member/<str:username>', views.block_member_admin_items, name ='block_member_items'),
    path('dashboard/admin_items/unblock_member/<str:username>', views.unblock_member_admin_items, name ='unblock_member_items'),
    path('dashboard/admin_users/edit_details/<str:username>', views.edit_details, name='edit_details'),
]