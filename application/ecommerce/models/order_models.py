from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=255,
        null=True, blank=True,
        unique=True,
        )
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_items = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=1,
        default='C',
        choices=(
            ("A", "Aprovado"),
            ("O", "Aberto"),
            ("C", "Criado"),
            ("R", "Reprovado"),
            ("P", "Pendente"),
            ("E", "Enviado"),
            ("F", "Finalizado"),
            ("X", "Cancelado"),
        )
    )

    def __str__(self):
        return f'Pedido {self.id} - {self.user.first_name} {self.user.last_name} - {self.status}'


class OrderItem(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=255,
        null=True, blank=True,
        unique=True,
        )
    product_name = models.CharField(max_length=65)
    product_id = models.PositiveBigIntegerField()
    product_variation = models.CharField(max_length=65)
    product_variation_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_amount = models.PositiveIntegerField(default=1)
    imagem = models.CharField(max_length=2560)

    def __str__(self):
        return f'Item do pedido {self.pedido.id} - {self.product_name}'
