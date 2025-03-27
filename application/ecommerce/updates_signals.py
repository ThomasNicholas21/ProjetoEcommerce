from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import ProductVariation

def update_product_stock(product):
    variations_stock = product.productvariation_set.aggregate(total=models.Sum('stock'))
    product.stock = variations_stock['total'] or 0
    product.save(update_fields=['stock'])

@receiver(post_save, sender=ProductVariation)
def update_stock_on_save(sender, instance, **kwargs):
    update_product_stock(instance.produto)
