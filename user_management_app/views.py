from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.template import loader
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "base.html")


def signup(request):
    if request.method == "POST":
        form = None
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            pwd = request.POST['password']
            # pwd2 = request.POST['pwd2']  --> to confirm the pwd

            new_user = User.objects.create_user(username, email, pwd)
            new_user.first_name = fname
            new_user.last_name = lname
            new_user.save()
            messages.success(request, "User account created")
            # return redirect('signin')
            return redirect('/accounts/login')
    else:
        form = CreateUserForm()
    template = loader.get_template('registration/signup.html')
    context = {
    'form': form,
    }
    return HttpResponse(template.render(context, request))        

def signin(request):
    return render(request, "registration/login.html")

def logout(request):
    logout(request)
    messages.success(request, "User was logged out")
    return redirect("/accounts/login")