from django.core.management.base import BaseCommand
from faker import Faker
from club.models import Faltes, Client, Compte, HistoricPagaments, Inscripcio, Personal, Entrenador, Horari, Classe, SolicitudFederacio
from random import randint
from random import choices
from dateutil.relativedelta import relativedelta
import random
from datetime import datetime
from datetime import date


horas_clase = ('10:15', '11:15', '17:30', '18:15', '19:15', '20:15')
letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
horas_modalidad_0= {0: {'hora': '10:15', 'modalidad': 1}, 1: {'hora': '11:15', 'modalidad': 2}, 
2: {'hora': '17:30', 'modalidad': 2}, 3: {'hora': '18:15', 'modalidad': 1}, 
4: {'hora': '19:15', 'modalidad': 1}, 5: {'hora': '20:15', 'modalidad': 3}}
horas_modalidad_1= {0: {'hora': '10:15', 'modalidad': 1}, 1: {'hora': '11:15', 'modalidad': 4}, 
2: {'hora': '17:30', 'modalidad': 2}, 3: {'hora': '18:15', 'modalidad': 1}, 
4: {'hora': '19:15', 'modalidad': 1}, 5: {'hora': '20:15', 'modalidad': 3}}
horas_modalidad_2= {0: {'hora': '10:15', 'modalidad': 1}, 1: {'hora': '11:15', 'modalidad': 3}, 
2: {'hora': '17:30', 'modalidad': 2}, 3: {'hora': '18:15', 'modalidad': 1}, 
4: {'hora': '19:15', 'modalidad': 1}, 5: {'hora': '20:15', 'modalidad': 1}}
horas_modalidad_3= {0: {'hora': '10:15', 'modalidad': 1}, 1: {'hora': '11:15', 'modalidad': 2}, 
2: {'hora': '17:30', 'modalidad': 2}, 3: {'hora': '18:15', 'modalidad': 1}, 
4: {'hora': '19:15', 'modalidad': 1}, 5: {'hora': '20:15', 'modalidad': 2}}
horas_modalidad_4= {0: {'hora': '10:15', 'modalidad': 1}, 1: {'hora': '11:15', 'modalidad': 3}, 
2: {'hora': '17:30', 'modalidad': 4}, 3: {'hora': '18:15', 'modalidad': 4}, 
4: {'hora': '19:15', 'modalidad': 1}, 5: {'hora': '20:15', 'modalidad': 2}}

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
        lista_entrenadores={}
        print("Adding Entrenador in database:")
        for i in range(10):
            # print(i+1, end = '\r')
            # try:
            list_entrenador={}
            id = randint(10000000,99999999)
            nom = fake.unique.first_name()
            modalidad=1
            if i > 2:
                modalidad = randint(1,3)
            else:
                modalidad = i + 1
            list_entrenador["dni"]=id
            list_entrenador["modalidad"]=modalidad
            lista_entrenadores[i]=list_entrenador
                # apellido = fake.unique.last_name()
                # fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
                # telefono=randint(100000000,999999999)
                # direccion=fake.unique.address()
                # federacion=randint(1000000000000,99999999999999)
                # IBAN=random.choice(Compte.objects.all())
                # Entrenador.objects.create(numFederacio=federacion ,compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
            # except:
            #     pass

        def encontrar_entrenador_modalidad(modalidad_añadir):
            encontrado = False
            while not encontrado:
                entrenador=randint(0, len(lista_entrenadores)-1)
                modalidad=lista_entrenadores[entrenador]
                if (modalidad["modalidad"] == modalidad_añadir):
                    encontrado = True
                    return entrenador
        
        def se_hace_clase(dia, hora):
            if dia == 0:
                for clases in horas_modalidad_0:
                    clase = horas_modalidad_0[clases]
                    if hora == datetime.strptime(clase["hora"], '%H:%M').time():
                        return clase["modalidad"]
            if dia == 1:
                for clases in horas_modalidad_1:
                    clase = horas_modalidad_1[clases]
                    if hora == datetime.strptime(clase["hora"], '%H:%M').time():
                        return clase["modalidad"]
            if dia == 2:
                for clases in horas_modalidad_2:
                    clase = horas_modalidad_2[clases]
                    if hora == datetime.strptime(clase["hora"], '%H:%M').time():
                        return clase["modalidad"]
            if dia == 3:
                for clases in horas_modalidad_3:
                    clase = horas_modalidad_3[clases]
                    if hora == datetime.strptime(clase["hora"], '%H:%M').time():
                        return clase["modalidad"]
            if dia == 4:
                for clases in horas_modalidad_4:
                    clase = horas_modalidad_4[clases]
                    if hora == datetime.strptime(clase["hora"], '%H:%M').time():
                        return clase["modalidad"]
            return 4
        
        # print(lista_entrenadores)
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
            
        # print("Adding SolicitudFederacio in database:")
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

        # print("Adding Clases in database:")
        for i in range(3):
            print(i+1, end='\r')
            tipo=randint(1,2)
            date_clase=random.choice(Horari.objects.all())
            str_date_clase=str(date_clase).split(',')
            date_type=datetime.strptime(str_date_clase[0], '%Y-%m-%d ').date()
            time_type=datetime.strptime(str_date_clase[1], ' %H:%M:%S').time()
            model=se_hace_clase(date_type.weekday(), time_type)
            if model != 4:
                valor=str(choices([0,1], [0.1, 0.9]))
                valor=bool(int(valor[1]))
                id=encontrar_entrenador_modalidad(model)
                entrenador=lista_entrenadores[id]
                if  date_type.weekday() == 3:
                    if  time_type <  datetime.strptime('13:00', '%H:%M').time():
                        tipo=3
                elif  date_type.weekday() == 4:
                    if  time_type > datetime.strptime('17:00', '%H:%M').time():
                        tipo=3
                # Classe.objects.create(modalitat=model, tipus=tipo, realitzada=valor, coach=entrenador, horari=date_clase)
                numParticipants=randint(1,2)
                encontrado=False
                tipo=3
                for _ in range(numParticipants):
                    # try:
                    cliente_obj=Client.objects.get(DNI=18079603)
                    print(cliente_obj)
                    if tipo == 3:
                        solFederacio=cliente_obj.solicitudfederacio_set.all()
                        if solFederacio:
                            #import pdb; pdb.set_trace()
                            if solFederacio[0].concedida and solFederacio[0].dataCaducitat > date.today():
                                print("Puedo participar en la clase")
                                # cliente_obj.classes.add(Classe)
                    # except:
                    #     pass
            else:
                pass

        # print("Adding Faltas in database:")
        # for i in range(20):
        #     print(i+1, end = '\r')
        #     data=fake.date_between_dates(date_start=datetime(2015,1,1), date_end=datetime.now())
        #     personalF=Personal.objects.first()
        #     print(personalF)
        #     Faltes.objects.create(dataFalta=data, personal=personalF)
