from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Classe, Client, Entrenador, Personal

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    queryset=Client.objects.all()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'clientes': queryset},
    )

def cliente(request, cliente_DNI):
    cliente = Client.objects.get(DNI=cliente_DNI)
    return render(
        request,
        'cliente_info.html',
        context={'cliente_info': cliente},
    )

def cliente_modificar(request, cliente_DNI):
    cliente = Client.objects.get(DNI=cliente_DNI)
    return render(
        request,
        'cliente_modificar.html',
        context={'cliente_modificar': cliente},
    )
