from django.shortcuts import render, get_object_or_404
from .models import Blogger

def all_blogs(request):
    information=Blogger.objects.order_by('-date')  #normally we will use .objects.all()
    return render(request,'blog/all_blogs.html',{'jason':information})

def detail(request,blog_id):
    blogking= get_object_or_404(Blogger,pk=blog_id)
    return render(request,'blog/detail.html',{'id':blogking})
# Create your views here.
