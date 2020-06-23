from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('sacircle',views.sacircle,name='sacircle'),
    path('sacircleForm',views.sacircleForm,name='sacircleForm'),
]
