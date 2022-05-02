from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from requests import request
from product_listing_app.models import Post
from . import group_filters
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

# deletes members page
@user_passes_test(group_filters.is_member)
def members_page(request):
    users = User.objects.all()
    template = loader.get_template('web_app/members.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))
# loads admin users page
@user_passes_test(group_filters.is_admin_users)
def admin_manage_users(request):
    members = User.objects.filter(groups__name='members').values('username', 'id', 'groups__name')
    template = loader.get_template('web_app/admins_users.html')
    context = {
        'members' : members
    }
    return HttpResponse(template.render(context,request))
# loads admin items page
@user_passes_test(group_filters.is_admin_items)
def admin_manage_items(request):
    members = User.objects.filter(groups__name='members').values('username', 'id', 'groups__name')
    posts = Post.objects.all()
    template = loader.get_template('web_app/admins_items.html')
    context = {
        'members' : members,
        'posts' : posts,
    }
    return HttpResponse(template.render(context,request))
# deletes users for admin users page
@user_passes_test(group_filters.is_admin_users)
def delete_user_au(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return HttpResponse(admin_manage_users(request))
# deletes users for admin items page
@user_passes_test(group_filters.is_admin_items)
def delete_user_ai(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return HttpResponse(admin_manage_items(request))
# deletes post for admin items page
@user_passes_test(group_filters.is_admin_items)
def delete_post(request, post_title):
    print(post_title)
    post = Post.objects.get(post_title=post_title)
    post.delete()
    return HttpResponse(admin_manage_items(request))
@user_passes_test(group_filters.is_admin)
def admin_access(request):
    non_admin_users = User.objects.exclude(groups__name='admin_gp').values('username', 'id', 'groups__name')
    print(non_admin_users)
    posts = Post.objects.all()
    template = loader.get_template('web_app/admins.html')
    context = {
        'non_admin_users' : non_admin_users,
        'posts' : posts,
    }
    return HttpResponse(template.render(context,request))