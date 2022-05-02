from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from requests import request
from product_listing_app.models import Post
from . import group_filters
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
@user_passes_test(group_filters.is_member)
def members_page(request):
    users = User.objects.all()
    template = loader.get_template('web_app/members.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))
@user_passes_test(group_filters.is_admin_users)
def admin_manage_users(request):
    members = User.objects.filter(groups__name='members').values('username', 'id', 'groups__name')
    template = loader.get_template('web_app/admins_users.html')
    context = {
        'members' : members
    }
    return HttpResponse(template.render(context,request))
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