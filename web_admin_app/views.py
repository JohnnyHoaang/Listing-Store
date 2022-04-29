from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from requests import request
# Create your views here.
def members_page(request):
    users = User.objects.all()
    template = loader.get_template('web_app/members.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))

def admin_manage_users(request):
    import json 
    from django.core.serializers.json import DjangoJSONEncoder
    members = User.objects.filter(groups__name='members').values('username', 'id', 'groups__name')
    template = loader.get_template('web_app/admins_users.html')
    context = {
        'members' : members
    }
    return HttpResponse(template.render(context,request))