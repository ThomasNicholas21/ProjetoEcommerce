from django.contrib import admin
from ecommerce.models.profile_models import UserProfile
from django.contrib.auth.models import User

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'birth_date', 
    list_display_links = 'user',
    search_fields = 'user__username',
    list_per_page = 10
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 
