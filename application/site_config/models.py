from django.db import models
from utils.images.image_validator import resize_image
# Create your models here.

class SiteConfig(models.Model):
    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configuration"

    name = models.CharField(max_length=65, default='E-commerce | Change-me')
    address = models.TextField()
    contact_number = models.CharField(max_length=35)
    contact_email = models.EmailField(max_length=254)
    about = models.TextField()
    cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to="logo/Y%/%m", blank=True, default='')
    favicon = models.ImageField(upload_to="assets/favicon/%Y/%m", blank=True, default='') # inserir validaçöes de imagem futuramente

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        current_logo_name = str(self.logo.name)
        super().save(*args, **kwargs)
        favicon_changed = False
        logo_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)

        if self.logo:
            logo_changed = current_logo_name != self.logo.name
        
        if logo_changed:
            resize_image(self.logo, 64)


    def __str__(self):
        return self.name
    
class SocialMidiaLinks(models.Model):
    class Meta:
        verbose_name = "Social Midia Link"
        verbose_name_plural = "Social Midia Links"

    name = models.CharField(max_length=35)
    urls = models.URLField(
        max_length=200, 
        blank=True, 
        null=True, help_text='Insira o Link da Rede Social'
        )
    new_tab = models.BooleanField(default=False)
    socialmidiaicon = models.ImageField(upload_to="icon/%Y/%m", blank=True, default='')
    site_config = models.ForeignKey(
        SiteConfig, on_delete=models.CASCADE,
        blank=True, null=True, default=None
        )
    
    def save(self, *args, **kwargs):
        current_socialmidiaicon_name = str(self.socialmidiaicon.name)
        super().save(*args, **kwargs)
        socialmidiaicon_changed = False

        if self.socialmidiaicon:
            socialmidiaicon_changed = current_socialmidiaicon_name != self.socialmidiaicon.name

        if socialmidiaicon_changed:
            resize_image(self.socialmidiaicon, 24)
    
    def __str__(self):
        return self.name