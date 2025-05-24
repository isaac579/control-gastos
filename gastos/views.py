from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm
#from django_filters import FilterView
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.db.models import Sum
from django.http import JsonResponse
from django.http import HttpResponse
from gastos.models import Gasto
from openpyxl import  Workbook
#from .filters import GastoFilter



def exportar_excel(request):
    gasto_filter = GastoFilter(request.GET, queryset=Gasto.objects.all())

    wb = Workbook()
    ws = wb.active
    ws.title = "Gastos filtrados"
#    ws.append(['Fecha', 'Categoria', 'Descripcion', 'Monto'])

    ws.append(['Fecha', 'Descripcion', 'Categoria', 'Monto'])

    for gasto in  gasto_filter.qs:
        ws.append([gasto.fecha, gasto.descripcion, gasto.categoria, gasto.monto])

   # Respuesta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Gastos_filtrados.xlsx'
    wb.save(response)
    return response


def vista_grafica(request):
    return render(request, 'gastos/grafica.html')


def grafica_gastos(request):
    datos = (
        Gasto.objects.values('categoria')
        .annotate(total=Sum('gasto'))
        .order_by('-total')
    )
    categorias = [d['categoria'] for d in datos]
    totales = [float(d['total']) for d in datos]
    return JsonResponse({
        'categorias': categorias,
        'totales': totales

    })



class GastoFilter(django_filters.FilterSet):
    fecha = django_filters.DateFromToRangeFilter(label='Rango de fechas')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    categoria = django_filters.CharFilter(lookup_expr='icontains', label='Categoria')


    class Meta:
     model = Gasto
     fields = ['fecha','descripcion','categoria']


#def lista_gastos(request):
#    gastos = Gasto.objects.all().order_by('-fecha')
#    total = sum(g.monto for g in gastos)
#    return render(request, 'gastos/lista_gastos.html', {'gastos': gastos, 'total': total})

def lista_gastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    gasto_filter = GastoFilter(request.GET, queryset=gastos)
    total = sum(g.monto for g in gasto_filter.qs)
    return render(request, 'gastos/lista_gastos.html',{
        'filter': gasto_filter,
        'total': total
    })

def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')
    else:
        form = GastoForm()
    return render(request, 'gastos/agregar_gasto.html', {'form': form})
