from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),  
    path('profile/', views.profile, name='profile'), 
    path('change_password/', views.change_password, name='change_password'), 
]