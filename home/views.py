from django.shortcuts import render, get_object_or_404
from home.models import Post
from pages.models import ContactInfo
from django.views import generic
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def contact(request):
    contact = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact': contact})


def about(request):
    return render(request, 'about.html')


# def post(request, slug):
    
#     post = Post.objects.get(slug=slug)
#     tags = Post.objects.all(tag)
#     return render(request, 'blog.html', {'post': post, 'tags': tags})
    
class PostList(generic.ListView):
    model = Post
    template_name = 'blog.html'
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
        
        return context