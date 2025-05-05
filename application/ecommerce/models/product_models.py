from django.db import models
from utils.slug.slug_gen import new_slug
from utils.images.image_validator import resize_image
from utils.validators.validate_image import is_png_svg
from django.utils.safestring import mark_safe

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=45)
    slug = models.SlugField(
        max_length=255, default=None,
        null=True, blank=True,
        unique=True,
        )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slug(self.name, 5)
        else:
            self.slug += new_slug('category-', 5)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
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
    stock = models.IntegerField(
        blank=False, 
        default=0, 
        null=True,
        verbose_name='Estoque total',
        help_text=mark_safe(
            "Essa campo será preenchido conforme o estoque for preenchido. <br>"
            "Em variações, basta colocar quantos produtos."
            )
        )
    active = models.BooleanField(default=True, blank=False)
    category = models.ManyToManyField(Category, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slug(self.name, 5)

        super_save = super().save(*args, **kwargs)
        
        if self.productvariation_set:
            variations_stock = self.productvariation_set.aggregate(total=models.Sum('stock'))
            self.stock = variations_stock['total']
            return super().save(update_fields=['stock'])

        return super_save

    def __str__(self):
        return self.name


class ProductVariation(models.Model):
    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'

    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)
    product_image = models.ImageField(
        upload_to="products/%Y/%m", 
        blank=True, default="products/defaults/product_default.png",
        validators=[is_png_svg,]
        )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    stock = models.IntegerField(blank=False, default=0, help_text="Coloque quantos produtos tem em estoque.")

    def save(self, *args, **kwargs):
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
