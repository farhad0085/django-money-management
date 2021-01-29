from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_utc', 'updated_utc']

admin.site.register(Tag, TagAdmin)
