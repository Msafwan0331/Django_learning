from django.shortcuts import render
from .models import Student


# Create your views here.
def new_app(request):
    Students=Student.objects.all()
    return render(request, "firstapp/new.html", {"Students": Students})
