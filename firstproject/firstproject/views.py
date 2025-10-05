from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    # return HttpResponse('hello from Django')
    return render (request,'index.html')
def welcome(request):
    return HttpResponse('Welcome to the day first of django')
