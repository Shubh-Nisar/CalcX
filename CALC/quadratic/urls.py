from django.urls import path

from . import views

urlpatterns=[
    path('quadratic',views.quadratic,name='quadratic'),
    # path('quadraticForm',views.quadraticForm,name='quadraticForm'),
]