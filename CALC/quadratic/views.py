import math
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quadratic(request):
    return render(request,'quadratic.html')

def quadraticForm(request):

    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    c = int(request.POST['num3'])

    x = (-b + math.sqrt(b*b-4*a*c))/2*a
    y = (-b - math.sqrt(b*b-4*a*c))/2*a

    
    return render(request,'quadratic.html',{'result1':x,'result2':y})