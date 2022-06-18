from django.shortcuts import render
# Create your views here.
from .models import Entrenador
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
    entrenador = Entrenador.objects.get(DNI=entrenador)
    return render(
        request,
        'entrenador/entrenador_info.html',
        context={'entrenador_info': entrenador},
    )
