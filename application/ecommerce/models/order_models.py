from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_value = models.FloatField()
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

