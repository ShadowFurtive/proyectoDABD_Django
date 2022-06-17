from django.urls import path, include, re_path

from . import views, clients, federacio, classe

urlpatterns = [
    path('', views.index, name='index'),
    
    # URL FEDERACIONS
    path(r'classe', classe.classe_general, name="classes"),

    # URL FEDERACIONS
    path(r'federacio', federacio.federacions_general, name="federacions"),
    # URL CLIENTS
    path(r'cliente/create/', clients.cliente_create, name='cliente_create'),
    path(r'cliente/<slug:cliente_DNI>/', clients.cliente, name='cliente_dni'),
    path(r'cliente/modificar/<slug:cliente_DNI>/', clients.cliente_modificar, name='cliente_modificar'),
    path(r'delete_cliente/<slug:cliente_DNI>', clients.delete_cliente, name='delete_cliente'),
    path(r'cliente', clients.cliente_general, name="cliente"),
]