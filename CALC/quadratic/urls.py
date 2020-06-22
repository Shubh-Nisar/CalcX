from django.urls import path

from . import views

urlpatterns=[
    path('quadratic',views.quadratic,name='quadratic')
]