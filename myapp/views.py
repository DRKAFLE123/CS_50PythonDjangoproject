from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")
def dr(request):
    return HttpResponse("Hello I am DRkafle")
def aaryan(request):
    return HttpResponse("Hello I am Aaryan")
def greet(request,name): #because url is passing name parameter to this fun
    return HttpResponse(f"Hello {name}")