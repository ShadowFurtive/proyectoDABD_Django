from django.shortcuts import render
# Create your views here.
from .models import SolicitudFederacio, Client
from .filters import FederacioFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import BadRequest
from dateutil.relativedelta import relativedelta
from random import randint
from datetime import date
import random

letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def federacions_general(request):
    """
    Función vista para la página inicio del sitio.
    """

    federacions= SolicitudFederacio.objects.all().order_by('-data')
    myFilter = FederacioFilter(request.GET, queryset=federacions)
    federacions = myFilter.qs
    page = request.GET.get('page', 1)
    
    paginator = Paginator(federacions, 50)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        federacions = paginator.page(page)
    except PageNotAnInteger:
        federacions = paginator.page(1)
    except EmptyPage:
        federacions = paginator.page(paginator.num_pages)
    # Genera contadores de algunos de los objetos principales

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'federacio/federacions.html',
        context={'federacions': federacions, 'myFilter': myFilter, 'page_range': page_range},
    )

def activate_federacio(request, federacio_num):
    federacio_existeix = SolicitudFederacio.objects.filter(numero=str(federacio_num)).exists()
    if federacio_existeix:
        federacio =  SolicitudFederacio.objects.get(numero=str(federacio_num))

        # checkear que no tenga el cliente una federación activa:
        federacio_actives = SolicitudFederacio.objects.filter(client=federacio.client, concedida=True, dataCaducitat__gt=date.today()).count()
        if federacio_actives >= 1:
            raise BadRequest("Ya tiene una federación existente.")
        if not federacio.concedida:
            federacio.concedida=True
            numero_inscripcion_f=randint(10000000000000,99999999999999)
            num_federacio_existeix = SolicitudFederacio.objects.filter(numFederacio=numero_inscripcion_f).exists()
            while num_federacio_existeix:
                numero_inscripcion_f=randint(10000000000000,99999999999999)
                num_federacio_existeix = SolicitudFederacio.objects.filter(numFederacio=numero_inscripcion_f).exists()
            data_final = federacio.data + relativedelta(years=+1)
            federacio.dataCaducitat=data_final
            federacio.numFederacio=numero_inscripcion_f
            federacio.save()
    else:
        raise BadRequest("Federacio no existe.")

    return federacions_general(request)


def delete_federacio(request, federacio_num):
    federacio_existeix = SolicitudFederacio.objects.filter(numero=str(federacio_num)).exists()
    if federacio_existeix:
        SolicitudFederacio.objects.filter(numero=str(federacio_num)).delete()
        status="Ha sigut eliminada la federació amb número "+ str(federacio_num)
        context={'status': status}
    else:
        status="No ha sigut posible eliminar la federació amb número "+ str(federacio_num) + " ja que no existeix"
        context={'status': status}
    return render( 
        request,
        'federacio/federacio_delete.html',
        context=context
    )

def federacio_create(request):
    print(request.POST)
    if request.method == "POST":
        data = date.today()
        data_final=None
        numSolFederacio=random.choice(letras)+random.choice(letras)+str(randint(10000000,99999999))
        num_federacio_existeix = SolicitudFederacio.objects.filter(numero=numSolFederacio).exists()
        while num_federacio_existeix:
                numSolFederacio=random.choice(letras)+random.choice(letras)+str(randint(10000000,99999999))
                num_federacio_existeix = SolicitudFederacio.objects.filter(numero=numSolFederacio).exists()
        if request.POST.get("pagament"): 
            pagament = True
        else:
            pagament = False
        if not pagament: 
            concebuda = False
        else:
            if request.POST.get("concebuda"): 
                concebuda = True
            else:
                concebuda = False
        if request.POST.get("dni"): 
            dni = request.POST.get("dni")
        else:
            raise BadRequest("dni necesario.")

        if pagament and concebuda:
            data_final = data + relativedelta(years=+1)
            numero_inscripcion_f=randint(10000000000000,99999999999999)
            num_federacio_existeix = SolicitudFederacio.objects.filter(numFederacio=numero_inscripcion_f).exists()
            while num_federacio_existeix:
                numero_inscripcion_f=randint(10000000000000,99999999999999)
                num_federacio_existeix = SolicitudFederacio.objects.filter(numFederacio=numero_inscripcion_f).exists()
        else:
            numero_inscripcion_f=None
        client = Client.objects.get(DNI=dni)
        federacio_actives = SolicitudFederacio.objects.filter(client=client, concedida=True, dataCaducitat__gt=date.today()).count()
        if federacio_actives >= 1:
            raise BadRequest("Ya tiene una federación existente.")

        SolicitudFederacio.objects.create(numero=numSolFederacio, pagament=pagament, concedida=concebuda, data=data, numFederacio=numero_inscripcion_f, dataCaducitat=data_final, client=client)
        return federacions_general(request)
    return render(
        request,
        'federacio/federacions_create.html',
        context={},
    )