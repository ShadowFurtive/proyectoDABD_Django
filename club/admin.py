from django.contrib import admin

from .models import HistoricPagaments, Inscripcio, PersonaTemplate, Compte, Client, Personal, Entrenador, SolicitudFederacio

admin.site.register(PersonaTemplate)
admin.site.register(Compte)
admin.site.register(Client)
admin.site.register(Entrenador)
admin.site.register(Personal)
admin.site.register(Inscripcio)
admin.site.register(HistoricPagaments)
admin.site.register(SolicitudFederacio)