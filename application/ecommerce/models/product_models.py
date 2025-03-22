from django.db import models
from utils.slug.slug_gen import new_slug
from utils.images.image_validator import resize_image
from utils.validators.validate_image import is_png_svg

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
        max_length=255,
        null=True, blank=True,
        unique=True,
        )
    short_description = models.CharField(max_length=128)
    long_description = models.TextField()
    product_image = models.ImageField(
        upload_to="products/%Y/%m", 
        blank=True, default="",
        validators=[is_png_svg,]
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_type = models.CharField(
        default=None, max_length=1, choices=PRODUCTS_TYPE,
        help_text=(
            'Produto "Simples" não possui variações, sendo ele único. '
            'Já o produto "Variável" é um produto cujo possui variações, por exemplo, cores e tamanhos diferentes.'
            )
    )
    stock = models.IntegerField(blank=False, default=0, help_text="Coloque quantos produtos tem em estoque.")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slug(self.name, 5)

        current_pruduct_image_name = str(self.product_image.name)
        super_save = super().save(*args, **kwargs)
        product_image_changed = False

        if self.product_image:
            product_image_changed = current_pruduct_image_name != self.product_image.name
        
        if product_image_changed:
            resize_image(self.product_image)

        return super_save

    def __str__(self):
        return self.name
