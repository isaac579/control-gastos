from django.db import models

class Gasto(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"
