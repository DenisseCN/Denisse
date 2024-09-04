from django.db import models
from django.contrib.auth.models import User
from apps.poleras.models import Polera

class CarritoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    polera = models.ForeignKey(Polera, on_delete=models.DO_NOTHING)
    talla = models.CharField(max_length=2)
    cantidad = models.IntegerField(default=1)
    precio = models.IntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad}x {self.polera.nombre} - Talla {self.talla}"
