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




