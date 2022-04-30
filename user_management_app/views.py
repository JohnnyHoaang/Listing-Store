from django.shortcuts import render, redirect
from user_management_app.models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, "base.html")


def signup(request):
    form = None
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        print(f"valid: {form.is_valid()}")
        if form.is_valid(): 
            new_user = form.save(commit = False)
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            from PIL import Image
            avatar = Image.open(r'static/default_avatar.png')
            profile = Profile(user=new_user, avatar=avatar)
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
