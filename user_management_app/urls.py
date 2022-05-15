from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from web_admin_app import views as wv
urlpatterns = [
    path('', views.index, name='index'), 
    path('category_filter/', views.category_filter_query, name='category'),
    path('status_filter', views.status_filter_query, name = 'status'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),  
    path('profile/', views.profile, name='profile'), 
    path('change_password/', views.change_password, name='change_password'), 
    path('dashboard/', wv.redirect_dashboard_page, name='redirect_dashboard_page')
]