import math
from django.db.models.expressions import Func
from django.db.models.fields import FloatField, IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quadratic(request):
    return render(request,'quadratic.html')

# def quadraticForm(request):

#     a = int(request.POST['num1'])
#     b = int(request.POST['num2'])
#     c = int(request.POST['num3'])

#     d=(b*b-4*a*c)
#     x = (-b + math.sqrt(b*b-4*a*c))/(2*a)
#     y = (-b - math.sqrt(b*b-4*a*c))/(2*a)

    
#     return render(request,'quadratic.html',{'result1':x,'result2':y})