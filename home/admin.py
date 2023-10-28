from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Post, Comment

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)



