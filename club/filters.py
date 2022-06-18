from cgitb import lookup
from codecs import lookup_error
import django_filters
from .models import *

class PersonaFilter(django_filters.FilterSet):
    
    class Meta:
        model = PersonaTemplate
        fields = ['DNI', 'nom']




class FederacioFilter(django_filters.FilterSet):
    class Meta:
        model = SolicitudFederacio
        fields = ['numero', 'concedida', 'numFederacio']



# class ClasseFilter(django_filters.FilterSet):
#     class Meta:
#         model = Classe
#         fields = ['modalitat', 'tipus']
