from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vcircle(request):
    return render(request,'vcircle.html')

def vcircleForm(request):
    radius = int(request.POST['radCircle'])
    volume = (4 * 3.14 * radius * radius * radius) / 3
    return render(request, 'vcircle.html', {'volume':volume})