from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('asector',views.asector,name='asector'),
    path('asectorForm', views.asectorForm, name='asectorForm'),
]
