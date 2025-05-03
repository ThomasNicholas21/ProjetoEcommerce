from django.contrib import admin
from ecommerce.models.order_models import Order, OrderItem
# Register your models here.


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]
