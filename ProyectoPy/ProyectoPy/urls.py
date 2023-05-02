from django.contrib import admin
from django.urls import path
from ProyectoPy.views import saludo, segunda_vista, probandoTemplate
from proyectoapp.views import producto

 

urlpatterns = [

    path("admin/", admin.site.urls),

    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('probandoTemplate/', probandoTemplate),
    path('producto/',producto),



]

