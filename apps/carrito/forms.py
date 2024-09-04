from django import forms
from django import forms
from .models import CarritoItem

class CarritoForm(forms.ModelForm):
    class Meta:
        model = CarritoItem
        fields = (
            'user',
            'polera',
            'talla',
            'cantidad',
            'precio',
            'creado_en'
        )
        labels = {
            'fotografia': 'Fotografía',
            'nombre': 'Nombre',
            'color': 'Color',
            'precio': 'Precio',
            'stock_S': 'Stock S',
            'stock_M': 'Stock M',
            'stock_L': 'Stock L',
            'stock_XL': 'Stock XL',
            
            'user': 'Usuario',
            'polera': 'Tipo polera',
            'talla': 'Talla',
            'cantidad': 'Cantidad',
            'precio': 'Precio',
            'creado_en': 'Fecha creación'
        }

