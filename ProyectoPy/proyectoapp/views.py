from django.shortcuts import render
from proyectoapp.models import Producto
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'proyectoapp/inicio.html')
def producto(request):
    return render(request,'proyectoapp/producto.html')
def cliente(request):
    return render(request,'proyectoapp/cliente.html')
def vendedor(request):
    return render(request,'proyectoapp/vendedor.html')

