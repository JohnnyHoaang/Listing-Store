from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
# Create your views here.
def index(request):
    users = User.objects.all()
    template = loader.get_template('web_app/members.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))