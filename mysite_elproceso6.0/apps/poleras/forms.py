from django import forms
from .models import Polera

class PoleraForm(forms.ModelForm):
    class Meta:
        model = Polera
        fields = (
            'fotografia',
            'nombre',
            'color',
            'precio',
            'stock_S',
            'stock_M',
            'stock_L',
            'stock_XL',
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
        }
        widgets = {
            'fotografia': forms.FileInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_S': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_M': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_L': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_XL': forms.NumberInput(attrs={'class': 'form-control'}),
        }
