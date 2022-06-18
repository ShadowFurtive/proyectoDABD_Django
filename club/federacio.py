from django.shortcuts import render
# Create your views here.
from .models import SolicitudFederacio
from .filters import FederacioFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import BadRequest
from dateutil.relativedelta import relativedelta
from random import randint
from datetime import date

def federacions_general(request):
    """
    Función vista para la página inicio del sitio.
    """

    federacions= SolicitudFederacio.objects.all()
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
    if request.method == "POST":
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