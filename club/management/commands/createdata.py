from django.core.management.base import BaseCommand
from faker import Faker
from club.models import Faltes, Client, Compte, HistoricPagaments, Inscripcio, Personal, Entrenador, Horari, Classe, SolicitudFederacio
from random import randint
from random import choices
from dateutil.relativedelta import relativedelta
import random
from datetime import datetime


horas_clase = ('10:15', '11:15', '17:30', '18:15', '19:15', '20:15')
letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def r(lim):
    return randint(0, lim-1)

class Command(BaseCommand):
    help = "Generator data"

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')
        
        # print("Adding Comptes in database: ")
        # for i in range(100):
        #     print(i+1, end = '\r')
        #     try:
        #         d = fake.unique.iban()
        #         Compte.objects.create(IBAN=d)
        #     except:
        #         pass

        # print("Adding Personal in database:")
        # for i in range(1):
        #     print(i+1, end = '\r')
        #     try:
        #         id = randint(10000000,99999999)
        #         nom = fake.unique.first_name()
        #         apellido = fake.unique.last_name()
        #         fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
        #         telefono=randint(100000000,999999999)
        #         direccion=fake.unique.address()
        #         IBAN=random.choice(Compte.objects.all())
        #         Personal.objects.create(compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
        #     except:
        #         pass
        
        # print("Adding Entrenador in database:")
        # for i in range(10):
        #     print(i+1, end = '\r')
        #     try:
        #         id = randint(10000000,99999999)
        #         nom = fake.unique.first_name()
        #         apellido = fake.unique.last_name()
        #         fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
        #         telefono=randint(100000000,999999999)
        #         direccion=fake.unique.address()
        #         federacion=randint(1000000000000,99999999999999)
        #         IBAN=random.choice(Compte.objects.all())
        #         Entrenador.objects.create(numFederacio=federacion ,compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
        #     except:
        #         pass

        # print("Adding Horarios in database:")
        # for i in range(200):
        #     print(i+1, end = '\r')
        #     date_clase= fake.date_between_dates(date_start=datetime(2022,5,1), date_end=datetime(2022,12,1))
        #     if date_clase.weekday() < 5:
        #         try:
        #             hora = horas_clase[r(len(horas_clase))]
        #             Horari.objects.create(data=date_clase, horario=hora)
        #         except:
        #             pass

        # print("Adding Clases in database:")
        # for i in range(80):
        #     print(i+1, end='\r')
        #     try:
        #         tipo=randint(1,2)
        #         model=randint(1,3)
        #         valor=str(choices([0,1], [0.1, 0.9]))
        #         valor=bool(int(valor[1]))
        #         entrenador=random.choice(Entrenador.objects.all())
        #         date_clase=random.choice(Horari.objects.all())
        #         str_date_clase=str(date_clase).split(',')
        #         date_type=datetime.strptime(str_date_clase[0], '%Y-%m-%d ').date()
        #         time_type=datetime.strptime(str_date_clase[1], ' %H:%M:%S').time()
        #         if  date_type.weekday() == 3:
        #             if  time_type <  datetime.strptime('13:00', '%H:%M').time():
        #                 tipo=3
        #         elif  date_type.weekday() == 4:
        #             if  time_type > datetime.strptime('17:00', '%H:%M').time():
        #                 tipo=3
        #         Classe.objects.create(modalitat=model, tipus=tipo, realitzada=valor, coach=entrenador, horari=date_clase)
        #     except:
        #         pass

        # print("Adding Clientes in database:")
        # for i in range(300):
        #     print(i+1, end = '\r')
        #     try:
        #         id = randint(10000000,99999999)
        #         nom = fake.unique.first_name()
        #         apellido = fake.unique.last_name()
        #         fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
        #         telefono=randint(100000000,999999999)
        #         direccion=fake.unique.address()
        #         domiciliat=str(choices([0,1], [0.4, 0.6]))
        #         domiciliat=bool(int(domiciliat[1]))
        #         IBAN=None
        #         if domiciliat==True:
        #             IBAN=random.choice(Compte.objects.all())
        #         cliente_obj=Client.objects.create(PagementDomiciliat=domiciliat, compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
        #         numClases=randint(5,30)
        #         for _ in range(numClases):
        #             try:
        #                 clase=random.choice(Classe.objects.all())
        #                 cliente_obj.classes.add(clase)
        #             except:
        #                 pass
        #     except:
        #         pass
            
        # print("Adding Inscripcio in database:")
        # for i in range(325):
        #     try:
        #         print(i+1, end = '\r')
        #         numero_inscripcion=randint(10000000000000,99999999999999)
        #         tipo=str(choices([1,2,3], [0.8, 0.1, 0.1]))
        #         fecha_inscripcion = fake.date_between_dates(date_start=datetime(2012,1,1), date_end=datetime.now())
        #         prop_insc=random.choice(Client.objects.all())
        #         Inscripcio.objects.create(numInscripcio=numero_inscripcion,tipus=tipo[1],dataInscripcio=fecha_inscripcion,client=prop_insc)
        #     except:
        #         pass
        
        # print("Adding HistoricPagament in database:")

        # inscripciones=Inscripcio.objects.all()
        # i=0
        # for inscripcio in inscripciones:
        #     try:
        #         print(i+1, end = '\r')
        #         str_inscripcio=str(inscripcio).split(',')
        #         date_type=datetime.strptime(str_inscripcio[2].strip(), '%Y-%m-%d').date()
        #         first_month=True
        #         lo_dejo=False
        #         pagament_f=50
        #         if str_inscripcio[1] == '2':
        #             pagament_f=25
        #         elif str_inscripcio[1] == '3':
        #             pagament_f=40
        #         while date_type < datetime.now().date() and not lo_dejo:
        #             print("Creando nuevo historico...")
        #             HistoricPagaments.objects.create(numInscripcio=inscripcio, data=date_type, Pagament=pagament_f)
        #             lo_dejo=str(choices([0,1], [0.7, 0.3]))
        #             lo_dejo=bool(int(lo_dejo[1]))

        #             if first_month:
        #                 date_type=date_type.replace(day=1)
        #                 first_month=False
        #             date_type = date_type + relativedelta(months=+1)
        #         i=+1
        #     except:
        #         pass
            
        print("Adding SolicitudFederacio in database:")
        # for i in range(100):
        #     print(i+1, end = '\r')
        #     try:
        #         numSolFederacio=random.choice(letras)+random.choice(letras)+str(randint(10000000,99999999))
        #         pagamentF=str(choices([0,1], [0.05, 0.95]))
        #         pagamentF=bool(int(pagamentF[1]))
        #         concedidaF=False
        #         if pagamentF:
        #             concedidaF=str(choices([0,1], [0.3, 0.7]))
        #             concedidaF=bool(int(concedidaF[1]))
        #         data=fake.date_between_dates(date_start=datetime(2018,1,1), date_end=datetime.now())
        #         numero_inscripcion=None
        #         data_final=None
        #         if concedidaF:
        #             numero_inscripcion=randint(10000000000000,99999999999999)
        #             data_final = data + relativedelta(years=+1)
        #         cliente_sol=random.choice(Client.objects.all())
        #         SolicitudFederacio.objects.create(numero=numSolFederacio, pagament=pagamentF, concedida=concedidaF, data=data, numFederacio=numero_inscripcion, dataCaducitat=data_final, client=cliente_sol)
        #     except:
        #         pass

        print("Adding Faltas in database:")
        for i in range(20):
            print(i+1, end = '\r')
            data=fake.date_between_dates(date_start=datetime(2015,1,1), date_end=datetime.now())
            personalF=Personal.objects.first()
            print(personalF)
            Faltes.objects.create(dataFalta=data, personal=personalF)