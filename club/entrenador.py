from msilib.schema import Class
from django.shortcuts import render
import datetime as DT
# Create your views here.
from .models import Entrenador, Classe
from .filters import PersonaFilter
from django.core.exceptions import BadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def entrenador_general(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    entrenadores= Entrenador.objects.all()
    myFilter = PersonaFilter(request.GET, queryset=entrenadores)
    entrenadores = myFilter.qs
    page = request.GET.get('page', 1)
    
    paginator = Paginator(entrenadores, 50)
    page_range = paginator.get_elided_page_range(number=page)
    print(paginator.num_pages)
    try:
        entrenadores = paginator.page(page)
    except PageNotAnInteger:
        entrenadores = paginator.page(1)
    except EmptyPage:
        entrenadores = paginator.page(paginator.num_pages)

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'entrenador/entrenador.html',
        context={'entrenadores': entrenadores, 'myFilter': myFilter, 'page_range': page_range},
    )

def entrenador_info(request, entrenador):
    trainer = Entrenador.objects.get(DNI=entrenador)
    classes_fetes = Classe.objects.filter(coach=trainer, realitzada=True).count()
    classes_no_fetes = Classe.objects.filter(coach=trainer, realitzada=False).count()
    return render(
        request,
        'entrenador/entrenador_info.html',
        context={'entrenador_info': trainer, 'classes_fetes': classes_fetes, 'classes_no_fetes': classes_no_fetes},
    )

def entrenador_classes(request, entrenador):
    trainer = Entrenador.objects.get(DNI=entrenador)
    classes = Classe.objects.filter(coach=trainer)
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
    return render(
        request,
        'entrenador/entrenador_classes.html',
        context={'entrenador': trainer, 'classes': classes,  'page_range': page_range},
    )

def entrenador_usemana(request, entrenador):
    trainer = Entrenador.objects.get(DNI=entrenador)
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)
    classes = Classe.objects.filter(coach=trainer, horari__data__gte=week_ago, horari__data__lte=today)
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
    return render(
        request,
        'entrenador/entrenador_classes.html',
        context={'entrenador': trainer, 'classes': classes,  'page_range': page_range},
    )
