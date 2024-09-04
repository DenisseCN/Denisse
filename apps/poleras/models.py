from django.db import models
from django.core.validators import MaxValueValidator

class Polera(models.Model):
    fotografia = models.ImageField(upload_to='poleras/')
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    precio = models.IntegerField(validators=[MaxValueValidator(9999999999)]) 
    stock_S = models.IntegerField(validators=[MaxValueValidator(999)], default=0)
    stock_M = models.IntegerField(validators=[MaxValueValidator(999)], default=0)
    stock_L = models.IntegerField(validators=[MaxValueValidator(999)], default=0)
    stock_XL = models.IntegerField(validators=[MaxValueValidator(999)], default=0)
    
    def __str__(self):
        return f"{self.nombre} - {self.color}" 
    