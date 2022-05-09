from os import unlink
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.template import loader
from requests import request
from product_listing_app.models import Post
from user_management_app.forms import CustomUserCreationForm, UserUpdateForm
from django.contrib import messages

from user_management_app.models import Profile
from web_admin_app.forms import PostUpdateForm
from . import group_filters
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def redirect_dashboard_page(request):
    user = request.user
    if group_filters.is_admin(user):
        return redirect('admin')
    elif group_filters.is_admin_items(user):
        return redirect('admin_items')
    elif group_filters.is_admin_users(user):
        return redirect('admin_users')
    elif group_filters.is_member(user):
        return redirect('members')
    return render(request, 'dashboard.html')


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

# deletes users 
def delete_user(request, username):
    if username is not None:
        user = User.objects.get(username=username)
        user.delete()
    return (redirect_dashboard_page(request))

def delete_post(request, title):
    if title is not None:
        post = Post.objects.get(title=title)
        post.delete()
    return (redirect_dashboard_page(request))
    
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

def add_member_table(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid(): 
            add_member(form)
            messages.success(request, 'Your account was successfully created! Please login to your account')
            return(redirect_dashboard_page(request))
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'web_app/add_users.html', context)   

def block_user(request, username):
    if username is not None:
        user = User.objects.get(username=username)
        user.is_active=False
        user.save()
    return(redirect_dashboard_page(request))

def unblock_user(request,username):
    if username is not None:
        user = User.objects.get(username=username)
        user.is_active=True
        user.save()
    return(redirect_dashboard_page(request))

def edit_user_details(request,username):
    user = User.objects.get(username=username)
    u_form = UserUpdateForm(instance=user)
    if request.method == 'POST':
        u_form = UserUpdateForm(data=request.POST, instance=user) 
        if u_form.is_valid():
            u_form.save()
            return redirect_dashboard_page(request)
    context = {
        'u_form':u_form
    }
    return render(request, 'web_app/edit_details.html', context)

def modify_group(request, username):
    user = User.objects.get(username=username)
    return render(request, 'web_app/modify_groups.html')
def edit_post(request, title):
    post = Post.objects.get(title=title)
    form = PostUpdateForm(instance=post)
    if request.method == 'POST':
        form = PostUpdateForm(data=request.POST, instance=post) 
        if form.is_valid():
            form.save()
            return redirect_dashboard_page(request)
    context = {
        'u_form': form
    }
    return render(request, 'web_app/edit_posts.html', context)