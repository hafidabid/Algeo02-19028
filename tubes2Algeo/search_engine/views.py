from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.conf.urls.static import static
from .supporter import *

def cobacek(request):
    return render(request,'searchbar.html',{})

def searchresult(req):
    if req.method=="POST":
        q = req.POST['pencarian']
        return render(req,'qresult.html',{})

def upfile(request):
    if(request.method=="POST"):
        print(request.POST)
        filename = request.FILES["upfile"].name
        fileext = getFileExtension(filename)
        if(fileext!=".txt"):
            return HttpResponse("unsuported file!, <a href='/' >return to homepage</a>")
        else:
            
            return HttpResponse("oke oce")
        