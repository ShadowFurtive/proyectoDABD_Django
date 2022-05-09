from django.contrib import admin

from .models import PersonaTemplate, Client, Personal, Entrenador, Compte, SolicitudFederacio 

admin.site.register(PersonaTemplate)
admin.site.register(Client)
admin.site.register(Entrenador)
admin.site.register(Personal)
admin.site.register(Compte)
admin.site.register(SolicitudFederacio)