from .views import indexView, aboutView,saveDataView
from django.urls import path

urlpatterns = [
    path("", indexView, name="index"),
    path("about/", aboutView, name="about"),
    path("save-data/", saveDataView, name="save_data"),

]

