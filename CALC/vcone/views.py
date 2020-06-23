from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vcone(request):
    return render(request,'vcone.html')

def vconeForm(request):
    radius = int(request.POST['vRadius'])
    height = int(request.POST['vHeight'])
    volume = (3.14 * radius * radius* height)/3
    return render(request,'vcone.html',{'volume':volume})
