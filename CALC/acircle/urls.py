from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('acircle', views.acircle, name='acircle'),
    path('acircleForm', views.acircleForm,name='acircleForm'),
]
