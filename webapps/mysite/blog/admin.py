from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
  list_display=('title', 'timestamp')
  list_filter=['timestamp']

admin.site.register(BlogPost, BlogPostAdmin)

