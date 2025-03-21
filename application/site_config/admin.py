from django.contrib import admin
from site_config import models

# Register your models here.

@admin.register(models.SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact_number', 
        'contact_email', 
        )
    list_display_links = 'name',
