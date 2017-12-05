from django.db import models
from django.contrib import admin
from _overlapped import NULL

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150,null=True)
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)