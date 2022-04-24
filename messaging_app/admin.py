from django.contrib import admin
from messaging_app.models import Message
from messaging_app.models import ThreadModel
# Register your models here.
admin.site.register(Message)
admin.site.register(ThreadModel)