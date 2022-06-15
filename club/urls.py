from django.urls import path
from . import views

urlpatterns = [
    # ex: /producte/
    path('', views.index, name='index'),
    # ex: /producte/5/
    path(r'cliente/<slug:cliente_DNI>/', views.cliente, name='cliente'),
    path(r'cliente/modificar/<slug:cliente_DNI>/', views.cliente_modificar, name='cliente_modificar'),
]