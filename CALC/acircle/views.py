from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def acircle(request):
    return render(request,'acircle.html')

def acircleForm(request):
    radius = 0
    radius = int(request.POST['radCircle'])
    area = 3.14*radius*radius
    return render(request, 'acircle.html', {'area':area})
