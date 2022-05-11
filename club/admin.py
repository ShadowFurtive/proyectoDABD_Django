from django.contrib import admin

from .models import Compte, Personal, Inscripcio, HistoricPagaments, Entrenador, Horari, Classe, Client, SolicitudFederacio, Faltes

admin.site.register(Compte)
admin.site.register(Personal)
admin.site.register(Inscripcio)
admin.site.register(HistoricPagaments)
admin.site.register(Entrenador)
admin.site.register(Horari)
admin.site.register(Classe)
admin.site.register(Client)
admin.site.register(SolicitudFederacio)
admin.site.register(Faltes)
