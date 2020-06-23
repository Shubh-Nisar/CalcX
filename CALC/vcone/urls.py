from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('vcone',views.vcone,name='vcone'),
    path('vconeForm',views.vconeForm,name='vconeForm'),
]
