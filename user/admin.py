from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone_number']

admin.site.register(UserProfile, UserProfileAdmin)
