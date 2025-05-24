from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_gastos, name='lista_gastos'),
    path('agregar/', views.agregar_gasto, name='agregar_gasto'),
    path('grafica/', views.vista_grafica, name='vista_grafica'),
    path('grafica/data/', views.grafica_gastos, name='grafica_gastos'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
]
