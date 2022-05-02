from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
import base64

# Create your views here.
def index(request):
    encoded_image = None
    if request.user.is_authenticated:
        if request.user.profile.avatar != None:
            encoded_image = base64.b64encode(request.user.profile.avatar).decode("utf-8")
    context = {
        'encoded_image': encoded_image
    }
    template = loader.get_template('base.html')
    return HttpResponse(template.render(context, request))


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
