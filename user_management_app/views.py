from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Account
from django.template.defaulttags import csrf_token

# Create your views here.
def index(request):
    return render(request, "authentication/signup.html")
    # return HttpResponse("Hello World")

# @csrf_token
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        # pwd2 = request.POST['pwd2']  --> to confirm the pwd

        new_user = Account.objects.create_user(username, fname, lname, email, pwd1)
        new_user.save()

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")