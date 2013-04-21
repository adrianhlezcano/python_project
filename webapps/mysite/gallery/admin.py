from django.contrib import admin
from gallery.models import Item, Photo

class PhotoInline(admin.StackedInline):
  model=Photo

class ItemAdmin(admin.ModelAdmin):
  inlines=[PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
