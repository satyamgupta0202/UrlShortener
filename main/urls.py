from django import views
from django.contrib import admin
from django.urls import path,include
from main import views
urlpatterns = [
    path('/createShorten',views.createShorten,name="shortUrl"),
    path('/createShorten/<str:id>' , views.redirectUrl , name="longUrl")
]