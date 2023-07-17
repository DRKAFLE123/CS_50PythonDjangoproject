from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path("", views.index , name="index"),
    path("<str:name>",views.greet, name='greet') , #it will pass the parameter (str:name)to greet fun
    path("dr/", views.dr , name="dr"),
    path("aaryan/",views.aaryan,name="Aaryan"),
]
