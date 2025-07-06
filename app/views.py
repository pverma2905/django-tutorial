from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homeSomthing(request):
    # return HttpResponse("My Home Page")
    return render(request, "index.html")
def aboutSomthing(request):
    return HttpResponse("My About Page")