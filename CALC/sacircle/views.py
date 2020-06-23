from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sacircle(request):
    return render(request,'sacircle.html')

def sacircleForm(request):
    radius = int(request.POST['radCircle'])
    area = 4 * 3.14 * radius * radius
    return render(request,'sacircle.html',{'area':area})    
