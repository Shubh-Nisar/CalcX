from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def shell(request):
    return render(request,'shell.html')

def shellForm(request):
    oRadius = int(request.POST['oRadius'])
    iRadius = int(request.POST['iRadius'])
    oRadiusCube = oRadius * oRadius * oRadius
    iRadiusCube = iRadius * iRadius * iRadius
    volume = (4 * 3.14 *(oRadiusCube-iRadiusCube))/3
    return render(request,'shell.html',{'volume':volume})
