from django.urls import path

from . import views

urlpatterns=[
    path('biquadratic',views.biquadratic,name='quadratic')
]