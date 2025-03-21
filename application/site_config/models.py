from django.db import models

# Create your models here.

class SiteConfig(models.Model):
    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    name = models.CharField(max_length=65, default='E-commerce | Change-me')
    address = models.TextField()
    contact_number = models.CharField(max_length=35)
    contact_email = models.EmailField(max_length=254)
    about = models.TextField()
    cnpj = models.CharField(max_length=18, unique=True, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to="logo/Y%/%m", blank=True, default='')
    favicon = models.ImageField(upload_to="assets/favicon/%Y/%m", blank=True, default='') # inserir validaçöes de imagem futuramente

    def __str__(self):
        return self.name
    