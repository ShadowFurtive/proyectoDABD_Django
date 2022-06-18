from django.shortcuts import render
# Create your views here.
from .models import Personal, Faltes
from .filters import PersonaFilter
from django.core.exceptions import BadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def personal_general(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    personals= Personal.objects.all()
    myFilter = PersonaFilter(request.GET, queryset=personals)
    personals = myFilter.qs
    page = request.GET.get('page', 1)
    
    paginator = Paginator(personals, 50)
    page_range = paginator.get_elided_page_range(number=page)
    print(paginator.num_pages)
    try:
        personals = paginator.page(page)
    except PageNotAnInteger:
        personals = paginator.page(1)
    except EmptyPage:
        personals = paginator.page(paginator.num_pages)

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'personal/personal.html',
        context={'personal': personals, 'myFilter': myFilter, 'page_range': page_range},
    )

def personal_info(request, personal):
    persona = Personal.objects.get(DNI=personal)
    return render(
        request,
        'personal/personal_info.html',
        context={'personal_info': persona},
    )

def personal_faltes(request, personal):
    persona = Personal.objects.get(DNI=personal)
    faltes = Faltes.objects.filter(personal=persona)
    return render(
        request,
        'personal/personal_faltes.html',
        context={'personal': persona, 'faltes': faltes},
    )