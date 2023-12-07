from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    content = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.content


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
    
    # def update_views(self, *args, **kwargs):
    #     self.views = self.views + 1
    #     super(Post, self).save(*args, **kwargs)
    
    
    
   
    



