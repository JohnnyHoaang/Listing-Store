from os import unlink
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.template import loader
from requests import request
from product_listing_app.models import Post
from user_management_app.forms import CustomUserCreationForm, UserUpdateForm
from django.contrib import messages

from user_management_app.models import Profile
from web_admin_app.forms import GroupUpdateForm, PostUpdateForm
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
    members = User.objects.filter(groups__name='members').values('username', 'id', 'groups__name', 'is_active')
    template = loader.get_template('web_app/admins_users.html')
    context = {
        'members' : members
    }
    return HttpResponse(template.render(context,request))
# loads admin items page
@user_passes_test(group_filters.is_admin_items)
def admin_manage_items(request):
    members = User.objects.filter(groups__name='members').values('username', 'id', 'groups__name', 'is_active')
    posts = Post.objects.all().values('title','category','price', 'flagged', 'pk', 'comment', 'rated' , 'likes')
    template = loader.get_template('web_app/admins_items.html')
    context = {
        'members' : members,
        'posts' : posts,
    }
    return HttpResponse(template.render(context,request))

@user_passes_test(group_filters.is_admin)
def admin_access(request):
    non_admin_users = User.objects.exclude(groups__name='admin_gp').values('username', 'id', 'groups__name', 'is_active')
    posts = Post.objects.all().values('title','category','price','flagged', 'pk' , 'comment' , 'rated', 'likes')
    template = loader.get_template('web_app/admins.html')
    context = {
        'non_admin_users' : non_admin_users,
        'posts' : posts,
    }
    return HttpResponse(template.render(context,request))

# deletes users 
def delete_user(request, username):
    if username is not None:
        user = User.objects.get(username=username)
        user.delete()
    return (redirect_dashboard_page(request))

def delete_post(request, pk):
    if pk is not None:
        post = Post.objects.get(pk=pk)
        post.delete()
    return (redirect_dashboard_page(request))
    

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
        return(redirect_dashboard_page(request))
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'web_app/add_users.html', context)   

def block_user(request,username):
    if username is not None:
        user = User.objects.get(username=username)
        if user.is_active:
            user.is_active=False
        else:
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
    form = GroupUpdateForm(instance=user)
    if request.method == 'POST':
        form = GroupUpdateForm(data=request.POST, instance=user) 
        if form.is_valid():
            form.save()
            return redirect_dashboard_page(request)
    context = {
        'form':form
    }
    return render(request, 'web_app/modify_groups.html', context)
    
def show_post(request, pk):
    post = Post.objects.get(pk=pk)
    query = get_object_or_404(Post, id=pk)
    like_count = query.get_count_likes()
    context = {
        'post': post, 
        'like_count' : like_count,
    }
    return render(request, 'web_app/show_post.html', context)

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
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

def flag_post(request, pk):
    if pk is not None:
        post = Post.objects.get(pk=pk)
        if post.flagged:
            post.flagged = False
        else:
            post.flagged = True
        post.save()
    return redirect_dashboard_page(request)



    