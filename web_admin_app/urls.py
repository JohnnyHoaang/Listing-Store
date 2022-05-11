from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/members', views.members_page, name='members'),
    path('dashboard/admin_users',views.admin_manage_users, name='admin_users'),
    path('dashboard/admin_items', views.admin_manage_items, name='admin_items'),
    path('dashboard/admin', views.admin_access, name='admin'),
    path('dashboard/delete_user/<str:username>' , views.delete_user, name='delete_user'),
    path('dashboard/delete_post/<str:title>' , views.delete_post, name='delete_posts'),
    path('dashboard/add_member', views.add_member_table, name='add_member'),
    path('dashboard/block_user/<str:username>', views.block_user, name ='block_users'),
    path('dashboard/unblock_user/<str:username>', views.unblock_user, name ='unblock_users'),
    path('dashboard/edit_details/<str:username>', views.edit_user_details, name='edit_user_details'),
    path('dashboard/modify_group/<str:username>', views.modify_group, name='modify_group'),
    path('dashboard/edit_post/<str:title>', views.edit_post, name='edit_posts'),
    path('dashboard/show_post/<str:title>', views.show_post, name='show_posts'),
    
]