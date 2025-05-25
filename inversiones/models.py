# inversiones/models.py
from django.db import models

class Inversion(models.Model):
    TIPO_CHOICES = [
        ('ahorro', 'Ahorro'),
        ('cripto', 'Criptomoneda'),
        ('bienes', 'Bienes Raíces'),
        ('otro', 'Otro')
    ]



    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    tipo_inversion = models.CharField(max_length=20, choices=TIPO_CHOICES, default='otro')

    def __str__(self):
        return f"{self.nombre} - ${self.monto}"

