from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Maggi(request):
    return HttpResponse("Hi i am Maggi Function")

def Tags(request):
    return HttpResponse("<marquee><h1>Hi i am Tags Function</h1></marquee>")

def Tag1(request):
    return HttpResponse("<i>Hi i am Tag1 Function<i>")

def Division(request):
    return HttpResponse("<h1 align='Center'>Hi i am Division tag</h1>")