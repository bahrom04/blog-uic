from django.db import models
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to='static/post/')
    title = models.CharField(max_length=256,)
    description = models.CharField(max_length=256,)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=256)

    # comment_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=128)
    email = models.EmailField()
    website = models.CharField(max_length=256, blank=True)
    message = models.TextField()

