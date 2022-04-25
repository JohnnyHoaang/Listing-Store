from django.shortcuts import render
from django.db.models import Q
from django.views import View
from django.contrib.auth.models import User
from messaging_app.models import ThreadModel
from models import ThreadModel
from forms import ThreadForm

# Create your views here.

def home(request):
    return render(request, 'messagingHome.html')

class ListTreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(reciever=request.user))

        context = {
            'threads' : threads
        }
        return render(request, 'social/inbox.html', context)

class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form' : form
        }

        return render(request, 'social/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')
        
        try: 
            reciever = User.objects.get(username=username)
        except: