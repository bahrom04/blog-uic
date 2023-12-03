from django.urls import path
from home.views import PostList
from home import views


urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("post/<slug:slug>", PostList.as_view(), name="post"),
]