from os import unlink
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.template import loader
from requests import request
from product_listing_app.models import Post
from user_management_app.forms import CustomUserCreationForm
from django.contrib import messages

from user_management_app.models import Profile
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
def delete_user(username):
    user = User.objects.get(username=username)
    user.delete()
# deletes users for admin users page
@user_passes_test(group_filters.is_admin_users)
def delete_user_admin_users(request, username):
    if username is not None:
        delete_user(username)
        return redirect('admin_users')
    return HttpResponse(admin_manage_users(request))
# deletes users for admin items page
@user_passes_test(group_filters.is_admin_items)
def delete_user_admin_items(request, username):
    if username is not None:
        delete_user(username)
        return redirect('admin_items')
    return HttpResponse(admin_manage_items(request))
# deletes post for admin items page
@user_passes_test(group_filters.is_admin_items)
def delete_post(request, post_title):
    if post_title is not None:
        post = Post.objects.get(post_title=post_title)
        post.delete()
        return redirect('admin_items')
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

def add_member(form):
    new_user = form.save(commit = False)
    new_user.first_name = form.cleaned_data['first_name']
    new_user.last_name = form.cleaned_data['last_name']
    new_user.save()
    g = Group.objects.get(name='members')
    g.user_set.add(new_user)
    with open('user_management_app/static/default_avatar.png', 'rb') as imagefile:
        bytestring = imagefile.read()
        profile = Profile(user=new_user, avatar=bytestring)
        profile.save()

@user_passes_test(group_filters.is_admin_users)
def add_member_users(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid(): 
            add_member(form)
            messages.success(request, 'Your account was successfully created! Please login to your account')
            return redirect('admin_users')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'web_app/add_users.html', context)   

@user_passes_test(group_filters.is_admin_items)
def add_member_items(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid(): 
            add_member(form)
            messages.success(request, 'Your account was successfully created! Please login to your account')
            return redirect('admin_items')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'web_app/add_users.html', context)   

def block_member(username):
    user = User.objects.get(username=username)
    user.is_active=False
    user.save()

def unblock_member(username):
    user = User.objects.get(username=username)
    user.is_active=True
    user.save()

@user_passes_test(group_filters.is_admin_users)
def block_member_admin_users(request, username):
    if username is not None:
        block_member(username)
        return redirect('admin_users')
    return HttpResponse(admin_manage_users(request))

@user_passes_test(group_filters.is_admin_items)
def block_member_admin_items(request, username):
    if username is not None:
        block_member(username)
        return redirect('admin_items')
    return HttpResponse(admin_manage_items(request))

@user_passes_test(group_filters.is_admin_users)
def unblock_member_admin_users(request, username):
    if username is not None:
        unblock_member(username)
        return redirect('admin_users')
    return HttpResponse(admin_manage_users(request))

@user_passes_test(group_filters.is_admin_items)
def unblock_member_admin_items(request, username):
    if username is not None:
        unblock_member(username)
        return redirect('admin_items')
    return HttpResponse(admin_manage_items(request))    

def redirect_dashboard_page(request):
    user = request.user
    if group_filters.is_admin(user):
        print("you are admin")
        return redirect('admin')
    elif group_filters.is_admin_items(user):
        print("you are admin items")
        return redirect('admin_items')
    elif group_filters.is_admin_users(user):
        print("you are admin user")
        return redirect('admin_users')
    elif group_filters.is_member(user):
        return redirect('members')
    
    
    template = 'dashboard.html'
    return render(request, 'dashboard.html')