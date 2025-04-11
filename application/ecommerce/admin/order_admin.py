from django.contrib import admin
from models.order_models import Pedido, ItemPedido
# Register your models here.


@admin.register(Pedido)
class UserProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(ItemPedido)
class UserProfileAdmin(admin.ModelAdmin):
    ...
