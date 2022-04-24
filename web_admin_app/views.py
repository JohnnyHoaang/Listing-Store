from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from requests import request
# Create your views here.
def index(request):
    users = User.objects.all()
    template = loader.get_template('web_app/members.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))

def admin_manage_users(request):
    import json 
    from django.core.serializers.json import DjangoJSONEncoder
    members = User.objects.filter(groups__name='members')
    # members_json = json.dumps(list(members.values('username', 'first_name', 'last_name', 'groups__name')))
    # with open("web_admin_app/static/data/members_data.json", "w") as file:
    #     json.dump(members_json, file)
    # # returns all members
    template = loader.get_template('web_app/admins_users.html')
    context = {
        'members' : members
    }
    return HttpResponse(template.render(context,request))

def json(request):
    members = User.objects.filter(groups__name='members')
    data = list(members.values('username', 'first_name', 'last_name', 'groups__name'))
    return JsonResponse(data, safe=False)