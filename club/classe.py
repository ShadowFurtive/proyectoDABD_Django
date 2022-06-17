from django.shortcuts import render
# Create your views here.
from .models import Classe
# from .filters import ClasseFilter
from django.core.exceptions import BadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

def classe_general(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    classes= Classe.objects.all()
    page = request.GET.get('page', 1)
    
    paginator = Paginator(classes, 5)
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
        context={'classes': classes},
    )