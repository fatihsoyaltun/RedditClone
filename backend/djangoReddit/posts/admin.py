from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['yazar',  'created_at']

admin.site.register(Post, PostAdmin)

admin.site.register(Toplulukolusturma)