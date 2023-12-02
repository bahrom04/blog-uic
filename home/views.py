from django.shortcuts import render
from home.models import Post
from pages.models import ContactInfo
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def contact(request):
    contact = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact': contact})


def about(request):
    return render(request, 'about.html')


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog.html', {'post': post})
    
