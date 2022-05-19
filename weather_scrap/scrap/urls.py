from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.input,name="home"),
    path('home/', views.home,name="home"),

    
]
