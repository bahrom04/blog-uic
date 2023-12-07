from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from app.models import Post
from django.views import generic
# Create your views here.

class HomeView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()
    
    


# def contact(request):
#     contact = ContactInfo.objects.first()
#     return render(request, 'contact.html', {'contact': contact})


class AboutView(generic.ListView):
    model = Post
    template_name = 'about.html'

# def post(request, slug):
    
#     post = Post.objects.get(slug=slug)
#     tags = Post.objects.all(tag)
#     return render(request, 'blog.html', {'post': post, 'tags': tags})
    
class PostList(generic.ListView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.get(slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)

        context['post'] = post

        tags = post.tag.all()
        context['tags'] = tags

        if post:
            post.views += 1
            post.save()
        
        return context
    
    