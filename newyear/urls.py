from django.contrib import admin
from django.urls import path
from newyear import views

urlpatterns = [
    path("", views.hello , name="hello"),
    path("check/", views.index , name="index"),

]