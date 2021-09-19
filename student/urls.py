from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('reject_list/',views.Reject_list.as_view(),name='reject'),
    path('application', views.application, name='application'),
    path('signup/',views.handleSignup,name='handleSignup'),
    path('Rejected_detail/<int:pk>/',views.Rejected_detail,name='r_detail'),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout',views.handleLogout,name='handleLogout')
]
