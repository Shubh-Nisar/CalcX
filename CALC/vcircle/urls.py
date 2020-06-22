from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('vcircle',views.vcircle,name='vcircle'),
    path('vcircleForm',views.vcircleForm,name='vcircleForm'),
]
