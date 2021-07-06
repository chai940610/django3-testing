from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    info= Project.objects.all()
    return render(request,'portfolio/personal.html',{'projects': info})
# Create your views here.
