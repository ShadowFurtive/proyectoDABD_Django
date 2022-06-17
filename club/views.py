from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Classe, Client, Entrenador, Personal, Compte, SolicitudFederacio, HistoricPagaments
from .filters import ClientFilter
from django.http import HttpResponse
from django.core.exceptions import BadRequest

def index(request):
    return render(
        request,
        'index.html',
        context={ 'num_clients': Client.objects.all().count(),
        'num_federacions': SolicitudFederacio.objects.all().count(),
        'num_classes': Classe.objects.all().count(),
        'num_pagaments': HistoricPagaments.objects.all().count() },
    )

def cliente_general(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    clientes=Client.objects.all()
    myFilter = ClientFilter(request.GET, queryset=clientes)
    clientes = myFilter.qs
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'clients/cliente.html',
        context={'clientes': clientes, 'myFilter': myFilter},
    )


def cliente(request, cliente_DNI):
    cliente = Client.objects.get(DNI=cliente_DNI)
    return render(
        request,
        'clients/cliente_info.html',
        context={'cliente_info': cliente},
    )

def cliente_modificar(request, cliente_DNI):
    print(request.POST)
    cliente = Client.objects.get(DNI=cliente_DNI)
    if request.POST.get("dni_input"):
        cliente_dni_nuevo = request.POST.get("dni_input")
        cliente_existe = Client.objects.filter(DNI=str(cliente_dni_nuevo)).exists()
        if not cliente_existe:
            cliente.DNI=str(cliente_dni_nuevo)
    if request.POST.get("nom_input"):
        cliente_nom_nuevo = request.POST.get("nom_input")
        cliente.nom = cliente_nom_nuevo
    if request.POST.get("cognom_input"):
        cliente_cognom_nuevo = request.POST.get("cognom_input")
        cliente.cognom = cliente_cognom_nuevo
    if request.POST.get("datanaix_input"):
        cliente_datanaix_nuevo = request.POST.get("datanaix_input")
        cliente.DataNaix = cliente_datanaix_nuevo
    if request.POST.get("telefon_input"): 
        cliente_tel_nuevo = request.POST.get("telefon_input")
        cliente.Telefon = cliente_tel_nuevo
    if request.POST.get("dir_input"):   
        cliente_dir_nuevo = request.POST.get("dir_input")
        cliente.direccio = cliente_dir_nuevo
    cliente.save()
    if request.POST.get("iban_num"): 
        cliente_iban_nuevo = request.POST.get("iban_num")
        if cliente.PagementDomiciliat == False:
            cliente.PagementDomiciliat = True
        iban_existe = Compte.objects.filter(IBAN=cliente_iban_nuevo).exists()
        if iban_existe:
            iban = Compte.objects.get(IBAN=cliente_iban_nuevo)
            Client.objects.filter(DNI=cliente_DNI).update(compteIBAN=iban)
            cliente_modificado = Client.objects.get(DNI=cliente_DNI)
            print(cliente_modificado)
        else:
            iban_nuevo = Compte.objects.create(IBAN=cliente_iban_nuevo)
            Client.objects.filter(DNI=cliente_DNI).update(compteIBAN=iban_nuevo)
    cliente = Client.objects.get(DNI=cliente_DNI)
    return render(
        request,
        'clients/cliente_modificar.html',
        context={'cliente_modificar': cliente},
    )


def cliente_create(request):
    print(request.POST)
    if request.method == "POST":
        if request.POST.get("dni_input"):
            cliente_dni_nuevo = request.POST.get("dni_input")
            cliente_existe = Client.objects.filter(DNI=str(cliente_dni_nuevo)).exists()
            if cliente_existe:
                raise BadRequest("DNI existe.")
        else:
             raise BadRequest("DNI necesario.")
        if request.POST.get("nom_input"):
            cliente_nom_nuevo = request.POST.get("nom_input")
        else:
            raise BadRequest("Nom necesario.")
        if request.POST.get("cognom_input"):
            cliente_cognom_nuevo = request.POST.get("cognom_input")
        else:
            raise BadRequest("Cognom necesario.")
        if request.POST.get("datanaix_input"):
            cliente_datanaix_nuevo = request.POST.get("datanaix_input")
        else:
            raise BadRequest("DataNaix necesario.")
        if request.POST.get("telefon_input"): 
            cliente_tel_nuevo = request.POST.get("telefon_input")
        else:
            raise BadRequest("Telefon necesario.")
        if request.POST.get("dir_input"):   
            cliente_dir_nuevo = request.POST.get("dir_input")
        else:
            raise BadRequest("Dirrecció necesario.")
        PagamentDomiciliat = False
        cliente_iban_nuevo = None
        if request.POST.get("iban_num"): 
            cliente_iban_nuevo = request.POST.get("iban_num")
            PagamentDomiciliat = True
            iban_existe = Compte.objects.filter(IBAN=cliente_iban_nuevo).exists()
            if iban_existe:
                cliente_iban_nuevo = Compte.objects.get(IBAN=cliente_iban_nuevo)
            else:
                cliente_iban_nuevo = Compte.objects.create(IBAN=cliente_iban_nuevo)

        cliente=Client.objects.create(PagementDomiciliat=PagamentDomiciliat, compteIBAN=cliente_iban_nuevo, DNI=cliente_dni_nuevo, nom=cliente_nom_nuevo, cognom=cliente_cognom_nuevo, DataNaix=cliente_datanaix_nuevo, Telefon=cliente_tel_nuevo, direccio=cliente_dir_nuevo)
        return render(
        request,
        'clients/cliente_info.html',
        context={'cliente_info': cliente},
        )
    return render(
        request,
        'clients/cliente_create.html',
        context={},
    )

def delete_cliente(request, cliente_DNI):
    print("hola")
    cliente_existe = Client.objects.filter(DNI=cliente_DNI).exists()
    if cliente_existe:
        Client.objects.filter(DNI=cliente_DNI).delete()
        status="Ha sido eliminado el cliente con DNI "+ str(cliente_DNI)
        context={'status': status}
    else:
        status="No ha sido posible eliminar el cliente con DNI "+ str(cliente_DNI) + " ya que no exista"
        context={'status': status}
    return render( 
        request,
        'clients/cliente_delete.html',
        context=context
    )
    