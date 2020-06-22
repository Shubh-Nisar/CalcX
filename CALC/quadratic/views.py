import math
from django.shortcuts import render

# Create your views here.

def quadratic(request):


    a = int(request.GET['num1'])
    b = int(request.GET['num2'])
    c = int(request.GET['num3'])

    x = (-b + math.sqrt(b*b-4*a*c))/2*a
    y = (-b - math.sqrt(b*b-4*a*c))/2*a

    
    return render(request,'quadratic.htm',{'result1':x},{'result2':y})