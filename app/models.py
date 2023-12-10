from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=256,)
    short_description = models.CharField(max_length=256,)
    content = RichTextUploadingField()
    tag = models.ManyToManyField(Tag, related_name='posts', blank=True)
    slug = models.SlugField(max_length=256)
    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        
        super(Post, self).save(*args, **kwargs)

    
    
   
    



