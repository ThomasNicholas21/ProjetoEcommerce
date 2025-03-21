from django.db import models


class Product(models.Model):
    PRODUCTS_TYPE = (
        ("S", 'Simples'),
        ("V", 'Variável'),
    )
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=65)
    slug = models.SlugField(
        max_length=255, default=None,
        null=True, blank=True,
        unique=True,
        )
    short_description = models.CharField(max_length=128)
    long_description = models.TextField()
    product_image = models.ImageField(
        upload_to="products/%Y/%m", 
        blank=True, default=""
        )
    price = models.FloatField()
    promotional_price = models.FloatField()
    product_type = models.CharField(
        default=None, max_length=1, choices=PRODUCTS_TYPE
    )
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
