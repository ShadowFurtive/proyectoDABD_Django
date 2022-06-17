from django.shortcuts import render
# Create your views here.
from .models import SolicitudFederacio
from .filters import FederacioFilter
from django.core.exceptions import BadRequest

def federacions_general(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    federacions= SolicitudFederacio.objects.all()
    myFilter = FederacioFilter(request.GET, queryset=federacions)
    federacions = myFilter.qs
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'federacio/federacions.html',
        context={'federacions': federacions, 'myFilter': myFilter},
    )