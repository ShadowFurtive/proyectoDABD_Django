
from django.shortcuts import render
# Create your views here.
from .models import Classe, Entrenador, Horari, Client
# from .filters import ClasseFilter
from django.core.exceptions import BadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

def classe_general(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    classes= Classe.objects.all().order_by('horari__data')
    page = request.GET.get('page', 1)
    
    paginator = Paginator(classes, 50)
    page_range = paginator.get_elided_page_range(number=page)
    print(paginator.num_pages)
    try:
        classes = paginator.page(page)
    except PageNotAnInteger:
        classes = paginator.page(1)
    except EmptyPage:
        classes = paginator.page(paginator.num_pages)
    # myFilter = ClasseFilter(request.GET, queryset=classes)
    # classes = myFilter.qs
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'classes/classes.html',
        context={'classes': classes, 'page_range': page_range},
    )

def classe_participants(request, data_par, hora, entrenador):
    horari = Horari.objects.get(data=data_par, horario=hora)
    coach = Entrenador.objects.get(DNI=entrenador)
    classe = Classe.objects.get(horari=horari, coach=coach)
    clientes = Client.objects.filter(classes=classe)
    return render(
        request,
        'classes/classes_participants.html',
        context={'clientes': clientes},
    )