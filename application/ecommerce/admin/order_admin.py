from django.contrib import admin
from ecommerce.models.order_models import Order, OrderItem
# Register your models here.


@admin.register(Order)
class UserProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(OrderItem)
class UserProfileAdmin(admin.ModelAdmin):
    ...
