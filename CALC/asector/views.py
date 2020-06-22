from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def asector(request):
    return render(request,'asector.html')

def asectorForm(request):
    radius = int(request.POST['radCircle'])
    angle = int(request.POST['radAngle'])
    angle = angle / 360
    area = 3.14 * radius * radius * angle
    return render(request,'asector.html',{'area':area})
