from django.contrib import admin

# Register your models here.
from .models import ContactInfo, ContactRequest, About

admin.site.register(ContactInfo)
admin.site.register(ContactRequest)
admin.site.register(About)
