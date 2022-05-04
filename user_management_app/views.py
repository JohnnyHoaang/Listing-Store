from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth import logout
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
import base64

# Create your views here.
def index(request):
    encoded_image = None
    if request.user.is_authenticated:
        # check if an avatar exists in the db and displays it
        if request.user.profile.avatar != None:
            encoded_image = base64.b64encode(request.user.profile.avatar).decode("utf-8")
    context = {
        'encoded_image': encoded_image
    }
    template = loader.get_template('base.html')
    return render(request, 'base.html', context)  


def signup(request):
    form = None
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid(): 
            new_user = form.save(commit = False)
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            with open('user_management_app/static/default_avatar.png', 'rb') as imagefile:
                bytestring = imagefile.read()
                profile = Profile(user=new_user, avatar=bytestring)
                profile.save()
            messages.success(request, 'Your account was successfully created! Please login to your account')
            return redirect('login')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/signup.html', context)     


def login(request):
    return render(request, "registration/login.html")


def logout(request):
    logout(request)


@login_required(login_url='/login')
def profile(request):
    encoded_image = None
    if request.user.is_authenticated:
        # check if an avatar exists in the db and displays it
        if request.user.profile.avatar != None:
            encoded_image = base64.b64encode(request.user.profile.avatar).decode("utf-8")
    if request.method == 'POST':
        u_form = UserUpdateForm(data=request.POST, instance=request.user) 
        if request.FILES.get('image', False):
            print(True)
            image = request.FILES['image'].file.read()
            Profile.objects.filter(user=request.user).update(avatar=image)
            encoded_image = base64.b64encode(image).decode("utf-8")
            return redirect('profile')
            
        if u_form.is_valid(): 
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'encoded_image': encoded_image,
        'u_form': u_form,
    }
    return render(request, 'registration/profile.html', context)


@login_required(login_url='/login')
def change_password(request):
    encoded_image = None
    if request.user.is_authenticated:
        # check if an avatar exists in the db and displays it
        if request.user.profile.avatar != None:
            encoded_image = base64.b64encode(request.user.profile.avatar).decode("utf-8")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error above.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'encoded_image': encoded_image,
        'form': form
    }
    return render(request, 'registration/change_password.html', context)