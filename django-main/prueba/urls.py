"""
URL configuration for misperris project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mascotas.views import *
from administracion.views import login_view, logout_view, registro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('galeria/', galeria, name="galeria"),
    path("registro/", registro, name="registro"),
    path("", inicio, name="inicio"),
    path("nosotros/", nosotros, name="nosotros"),
    path('administracion/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('solicitud/', crear_cliente_y_solicitud, name='solicitud'),
    path('solicitudes/', lista_solicitudes, name='solicitudes'),   
    # URL para el formulario de creación (Create)
    path('crear/',crear_mascota, name='crear_mascota'),
    
    # URL para editar una mascota específica (Update)
    path('editar/<int:pk>/', editar_mascota, name='editar_mascota'),
    
    # URL para eliminar una mascota (Delete)
    path('eliminar/<int:pk>/', eliminar_mascota, name='eliminar_mascota'),
    path('solicitudes/', lista_solicitudes, name='lista_solicitudes'),
    
    # URL para gestionar/editar una solicitud específica
    path('solicitudes/gestionar/<int:pk>/', gestionar_solicitud, name='gestionar_solicitud'),
    
    # URL para eliminar una solicitud (lleva a la confirmación)
    path('solicitudes/eliminar/<int:pk>/', eliminar_solicitud, name='eliminar_solicitud'),

    path('clientes/', lista_clientes, name='lista_clientes'),
    
    # 2. CREATE (Crear)
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    
    # 3. UPDATE (Actualizar)
    # <int:pk> coincide con el parámetro 'pk' en la vista editar_cliente
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    
    # 4. DELETE (Eliminar)
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),

]