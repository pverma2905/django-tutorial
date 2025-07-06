from app.views import homeSomthing, aboutSomthing
from django.urls import path

urlpatterns = [
    path("", homeSomthing, name="home"),
    path("about/", aboutSomthing, name="about"),
]

