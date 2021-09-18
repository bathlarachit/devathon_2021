from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
        path('contact', views.contact, name='contact'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout',views.handleLogout,name='handleLogout')
]
