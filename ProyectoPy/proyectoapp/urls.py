from django.urls import path
from proyectoapp import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('producto', views.producto, name="Producto"),
    path('cliente', views.cliente, name="Cliente"),
    path('vendedor', views.vendedor, name="Vendedor"),
]