from django.urls import path, include, re_path

from . import views, clients, federacio, classe, entrenador, personal

urlpatterns = [
    path('', views.index, name='index'),
    # URL PERSONAL      
    path(r'personal', personal.personal_general, name="personal"),
    path(r'personal/<slug:personal>/', personal.personal_info, name='personal_info'),
    path(r'personal/faltes/<slug:personal>/', personal.personal_faltes, name='personal_faltes'),
    # URL ENTRENADORES
    path(r'entrenador', entrenador.entrenador_general, name="entrenador"),
    path(r'entrenador/<slug:entrenador>/', entrenador.entrenador_info, name='entrenador_info'),
    path(r'entrenador/classes/<slug:entrenador>/', entrenador.entrenador_classes, name='entrenador_classes'),
    path(r'entrenador/usemana/<slug:entrenador>/', entrenador.entrenador_usemana, name='entrenador_usemana'),
    
    # URL classe
    path(r'classe_participants/(?P<data_par>\d{4}-\d{2}-\d{2})/$)/(?P<hora>\d{2}:\d{2}:\d{2})/<slug:entrenador>', classe.classe_participants, name='classe_participants'),
    path(r'classe', classe.classe_general, name="classes"),
    
    # URL FEDERACIONS
    path(r'create_federacio/create/', federacio.federacio_create, name='create_federacio'),
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