from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_value = models.FloatField()
    total_items = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=1,
        default='C',
        choices=(
            ("A", "Aprovado"),
            ("C", "Criado"),
            ("R", "Reprovado"),
            ("P", "Pendente"),
            ("E", "Enviado"),
            ("F", "Finalizado"),
            ("X", "Cancelado"),
        )
    )


class OrderItem(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=65)
    product_id = models.PositiveBigIntegerField()
    product_variation = models.CharField(max_length=65)
    product_variation_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_amount = models.PositiveIntegerField(default=1)
    imagem = models.CharField(max_length=2560)
