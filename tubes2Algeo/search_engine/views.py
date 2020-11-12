from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.conf.urls.static import static

def cobacek(request):
    return render(request,'searchbar.html',{})

def searchresult(req):
    if req.method=="POST":
        q = req.POST['pencarian']
        return render(req,'qresult.html',{})
