from lib2to3.pytree import Base
from django.core.management.base import BaseCommand
from faker import Faker
from club.models import Compte, Personal, Entrenador, Horari
from random import randint
import random
from datetime import datetime

horas_clase = ('10:15', '11:15', '17:30', '18:15', '19:15', '20:15')

def r(lim):
    return randint(0, lim-1)

class Command(BaseCommand):
    help = "Generator data"

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')
        
        print("Creating comptes in database: ")
        # for i in range(100):
        #     print(i+1, end = '\r')
        #     d = fake.unique.iban()
        #     Compte.objects.create(IBAN=d)
        print("Creating personal in database:")
        # for i in range(1):
        #     print(i+1, end = '\r')
        #     id = randint(10000000,99999999)
        #     nom = fake.unique.first_name()
        #     apellido = fake.unique.last_name()
        #     fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
        #     telefono=randint(100000000,999999999)
        #     direccion=fake.unique.address()
        #     IBAN=random.choice(Compte.objects.all())
        #     Personal.objects.create(compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
        
        print("Creating entrenador in database:")
        # for i in range(10):
        #     print(i+1, end = '\r')
        #     id = randint(10000000,99999999)
        #     nom = fake.unique.first_name()
        #     apellido = fake.unique.last_name()
        #     fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
        #     telefono=randint(100000000,999999999)
        #     direccion=fake.unique.address()
        #     federacion=randint(1000000000000,99999999999999)
        #     IBAN=random.choice(Compte.objects.all())
        #     Entrenador.objects.create(numFederacio=federacion ,compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)

        print("Añadiendo horarios in database:")
        for i in range(200):
            print(i+1, end = '\r')
            date_clase= fake.date_between_dates(date_start=datetime(2022,5,1), date_end=datetime(2022,12,1))
            if date_clase.weekday() < 4:
                hora = horas_clase[r(len(horas_clase))]
                entrenador=random.choice(Entrenador.objects.values('DNI'))
                db_horario = Horari.objects.create(data=date_clase, horario=hora)
                db_horario.entrenadores.set(entrenador)