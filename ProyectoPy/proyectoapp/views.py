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
            cliente = Cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),informacion['email'], informacion['profesion']) 
            cliente.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = clienteFormulario()
    return render(request,'proyectoapp/cliente.html', {"miFormulario": miFormulario})

def vendedor(request):
    if request.method == 'post':
        miFormulario = vendedorFormulario(request.post)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            vendedor = Vendedor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),informacion['email'], informacion['categoria']) 
            vendedor.save()
            return render(request, 'proyectoapp/inicio.html')
    else:
        miFormulario = vendedorFormulario()
    return render(request,'proyectoapp/vendedor.html', {"miFormulario": miFormulario})


def producto(request):
    return render(request,'proyectoapp/producto.html')

def buscar(request):
     if request.GET['categoria']:
          categoria = request.GET['categoria']
          categorias= Producto.objects.filter(categoria__icontains= categoria)

          return render(request,'proyectoapp/inicio.html', {"productos":categorias, "comisiones": categoria })
     else:
          respuesta= "No se encontraron datos"

     return render(request,"proyectoapp/inicio.html",{"respuesta":respuesta})


