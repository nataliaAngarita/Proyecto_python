from django.shortcuts import render
from proyectoapp.models import Producto, Cliente, Vendedor
from django.http import HttpResponse
from proyectoapp.forms import productoFormulario, clienteFormulario, vendedorFormulario
# Create your views here.
def inicio(request):
    return render(request, 'proyectoapp/inicio.html')
def producto(request):
    return render(request,'proyectoapp/producto.html')
def cliente(request):
    return render(request,'proyectoapp/cliente.html')
def vendedor(request):
    return render(request,'proyectoapp/vendedor.html')

def productos(request):
    if request.method == 'post':
        miFormulario = productoFormulario(request.post)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(int(informacion['id']),str(informacion['categoria']),str(informacion['nombre']), int(informacion['precio'])) 
            producto.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = productoFormulario()
    return render(request,'proyectoapp/ProductoFormulario.html', {"miFormulario": miFormulario})


def cliente(request):
    if request.method == 'post':
        miFormulario = clienteFormulario(request.post)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(int(informacion['id']),str(informacion['categoria']),str(informacion['nombre']), int(informacion['precio'])) 
            producto.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = productoFormulario()
    return render(request,'proyectoapp/ProductoFormulario.html', {"miFormulario": miFormulario})

