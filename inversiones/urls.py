# inversiones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_inversiones, name='lista_inversiones'),
    path('agregar/', views.agregar_inversion, name='agregar_inversion'),
]
