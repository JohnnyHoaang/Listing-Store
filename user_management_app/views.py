from django.shortcuts import render, redirect
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
            return redirect('index')
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'registration/signup.html', context)     


def logout(request):
    logout(request)
