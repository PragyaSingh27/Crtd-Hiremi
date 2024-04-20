from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path("", views.index, name='login'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("totalaccount", views.totalaccount, name='totalaccount'),
    path("profile", views.profile, name='profile')
    
    
]