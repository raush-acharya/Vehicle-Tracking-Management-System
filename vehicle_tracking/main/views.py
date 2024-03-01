from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def taskList(request):
    return HttpResponse("Vehicle Tracking")

def homePage(request):
    return render(request, 'index.html')

def otherPage(request):
    return render(request, 'other.html')