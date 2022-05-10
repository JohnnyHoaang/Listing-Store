from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views import View
from messaging_app.models import ThreadModel, Message
from .forms import MessageForm, ThreadForm

# Create your views here.

def home(request):
    return render(request, 'social/inbox.html')

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
            if ThreadModel.objects.filter(user=request.user, reciever=reciever).exists():
                thread = ThreadModel.objects.filter(user=request.user, reciever=reciever)[0]
                return redirect(f'thread/{thread.pk}')
            elif ThreadModel.objects.filter(user=reciever, reciever=request.user).exists():
                thread = ThreadModel.objects.filter(user=reciever, reciever=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                sender_thread = ThreadModel(user=request.user, reciever=reciever)
                sender_thread.save()
                thread_pk = sender_thread.pk
                return redirect('thread', pk=thread_pk)

        except:
            return redirect('create-thread')

class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(reciever=request.user))

        context = {
            'threads' : threads
        }
        return render(request, 'social/inbox.html', context)

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.reciever == request.user:
            reciever = thread.user
        else:
            reciever = thread.reciever
        message = Message(
            thread=thread,
            sender_user = request.user,
            reciever_user = reciever,
            body = request.POST.get('message')
        )
        message.save()
        return redirect('thread', pk=pk)

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = Message.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }
        return render(request, 'social/thread.html', context)