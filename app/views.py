from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def indexView(req):
    return render(req,"index.html")

def aboutView(req):
    return render(req,"about.html")

def saveDataView(req):
    print(req.POST)
    title = req.POST.get("title")
    description = req.POST.get("description")
    
    if not title or not description:
        messages.error(req, "Fill All Details")
        return redirect("/")
    else:
        messages.success(req,"Detail saved")   
        return redirect("/")