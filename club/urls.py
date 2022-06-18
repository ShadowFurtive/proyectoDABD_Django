from django.urls import path, include, re_path

from . import views, clients, federacio, classe, entrenador

urlpatterns = [
    path('', views.index, name='index'),
    
    # URL ENTRENADORES
    path(r'entrenador', entrenador.entrenador_general, name="entrenador"),
    path(r'entrenador/<slug:entrenador>/', entrenador.entrenador_info, name='entrenador_info'),

    # URL FEDERACIONS
    path(r'classe_participants/(?P<data_par>\d{4}-\d{2}-\d{2})/$)/(?P<hora>\d{2}:\d{2}:\d{2})/<slug:entrenador>', classe.classe_participants, name='classe_participants'),
    path(r'classe', classe.classe_general, name="classes"),
    
    # URL FEDERACIONS
    path(r'activate_federacio/<slug:federacio_num>/', federacio.activate_federacio, name='activate_federacio'),
    path(r'delete_federacio/<slug:federacio_num>/', federacio.delete_federacio, name='delete_federacio'),
    path(r'federacio', federacio.federacions_general, name="federacions"),
    # URL CLIENTS
    path(r'cliente/create/', clients.cliente_create, name='cliente_create'),
    path(r'cliente/<slug:cliente_DNI>/', clients.cliente, name='cliente_dni'),
    path(r'cliente_classes/<slug:cliente_DNI>/', clients.cliente_classes, name='cliente_classes'),
    path(r'cliente/modificar/<slug:cliente_DNI>/', clients.cliente_modificar, name='cliente_modificar'),
    path(r'delete_cliente/<slug:cliente_DNI>', clients.delete_cliente, name='delete_cliente'),
    path(r'cliente', clients.cliente_general, name="cliente"),
]