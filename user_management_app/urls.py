from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'), 
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    # path('signin/', LoginView.as_view(template_name='registration/signin.html'), name='signin'),
    # path('logout/', LogoutView.as_view(template_name='todo_app/logout.html'), name='logout'),
    path('accounts/', include("django.contrib.auth.urls"), name='accounts'),
   
]