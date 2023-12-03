from django.urls import path
from app.views import PostList, HomeView, AboutView
from app import views


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("index/", HomeView.as_view(), name="home"),
    # path("contact", views.contact, name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("post/<slug:slug>", PostList.as_view(), name="post"),
]