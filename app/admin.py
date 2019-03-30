from django.contrib import admin
from app import models

admin.site.register(models.category)
admin.site.register(models.banner)
@admin.register(models.article)
class articleAdmin(admin.ModelAdmin):
    list_display = ['type','title','views','ctime','mtime']
    list_per_page = 50
