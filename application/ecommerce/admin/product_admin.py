from django.contrib import admin
from ecommerce.models.product_models import Product, Category, ProductVariation

# Register your models here.

class VariationsTabularInline(admin.TabularInline):
    model = ProductVariation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'promotional_price',
    list_display_links = 'name',
    list_editable = 'price', 'promotional_price',
    search_fields = 'name', 'category__name'
    list_filter = 'category',
    prepopulated_fields = {'slug': ('name',)}
    inlines = [VariationsTabularInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 
    list_display_links = 'name',
    search_fields = 'name',
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'stock',
    list_display_links = 'name',
    search_fields = 'name', 'product__name',
