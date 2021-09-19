"""Devathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from Admin_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('detail/<int:pk>/',views.ViewDetail,name='look'),
    path('pending_list/',views.Pending.as_view(),name='p_list'),
    path('rejected_list/',views.Rejected.as_view(),name='r_list'),
    path('confirmed_list/',views.Confirmed.as_view(),name='c_list'),
    path('register/<int:pk>/',views.Registration,name='register'),
    path('Rejected_detail/<int:pk>/',views.Rejected_detail,name='r_detail'),
    path('student/', include('student.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
