from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('shell',views.shell,name='shell'),
    path('shellForm',views.shellForm,name='shellForm'),
]