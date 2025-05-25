import django_filters
from .models import Inversion
from django import forms
#class InversionFilter(django_filters.FilterSet):
#    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre contiene')
#    fecha = django_filters.DateFromToRangeFilter(label='Rango de fechas')
# filters.py
class InversionFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Nombre contiene',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha = django_filters.DateFromToRangeFilter(
        label='Rango de fechas',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'class': 'form-control'})
    )
    monto = django_filters.RangeFilter(
        label='Rango del monto',
        widget=django_filters.widgets.RangeWidget(attrs={'class': 'form-control', 'placeholder': 'Monto'})
    )

    tipo_inversion = django_filters.ChoiceFilter(
        choices=Inversion.TIPO_CHOICES,
        label='Tipo de inversión',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Inversion
        fields = ['nombre', 'fecha', 'monto']
