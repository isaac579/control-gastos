from django import forms
from .models import Inversion

class InversionForm(forms.ModelForm):
    class Meta:
        model = Inversion
        fields = ['nombre', 'monto', 'fecha', 'tipo_inversion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

