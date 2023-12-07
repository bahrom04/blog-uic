# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from app.models import Post

# @receiver(pre_save, sender=Post)
# def update_views(sender, instance, *args, **kwargs):
#     instance.views += 1
#     instance.save()