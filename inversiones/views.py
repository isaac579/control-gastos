from django.shortcuts import render, redirect
# Create your views here.
# inversiones/views.py
from .models import Inversion
from .forms import InversionForm
from .filters import InversionFilter

def lista_inversiones(request):
    inversiones = Inversion.objects.all()
    filtro = InversionFilter(request.GET, queryset=inversiones)
    total = sum(inversion.monto for inversion in filtro.qs)
    return render(request, 'inversiones/lista_inversiones.html', {'filter': filtro, 'total': total }) #'inversiones': inversiones})

def agregar_inversion(request):
    if request.method == 'POST':
        form = InversionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inversiones')
    else:
        form = InversionForm()
    return render(request, 'inversiones/agregar_inversion.html', {'form': form})
