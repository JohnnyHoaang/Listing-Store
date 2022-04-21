from django.urls import path
from . import views

urlpatterns = [
    path('product_listing', views.index, name='index'),
]
