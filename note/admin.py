from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'short_body', 'created_utc', 'updated_utc']

    def short_body(self, obj):
        return obj.body[:30]

admin.site.register(Note, NoteAdmin)
