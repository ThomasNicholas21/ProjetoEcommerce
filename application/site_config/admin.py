from django.contrib import admin
from site_config import models

# Register your models here.

class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = 'name', 'urls', 'new_tab',
    list_display_links = 'name', 'urls', 'new_tab',


class SocialMidiaLinkInline(admin.TabularInline):
    model = models.SocialMidiaLinks
    extra = 1


@admin.register(models.SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact_number', 
        'contact_email', 
        )
    list_display_links = 'name',
    inlines = SocialMidiaLinkInline,