from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Blogger)
admin.site.register(BlogPost)