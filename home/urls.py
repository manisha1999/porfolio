from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="ShopHome"),
    path("about/", views.about,name="aboutus"),
    path("skill/", views.skill,name="contactus"),
    path("project/", views.project,name="contactus"),
    path("proj/", views.proj,name="contactus"),
    path("other/", views.other,name="contactus"),
path("contact/", views.contact,name="contactus"),
path("register/", views.register,name="contactus"),
]
