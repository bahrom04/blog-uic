from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("post/<slug:slug>", views.post, name="post"),
]