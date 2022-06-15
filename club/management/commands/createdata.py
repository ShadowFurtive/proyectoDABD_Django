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
        
        print("Adding Personal in database:")
        for i in range(1):
            print(i+1, end = '\r')
        #     try:
            id = randint(10000000,99999999)
            id = str(id) + random.choice(letras)
            nom = fake.unique.first_name()
            apellido = fake.unique.last_name()
            fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
            telefono=randint(100000000,999999999)
            direccion=fake.unique.address()
            d = fake.unique.iban()
            IBAN=Compte.objects.create(IBAN=d)
            Personal.objects.create(compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
        # #     except:
        # #         pass
        lista_entrenadores={}
        print("Adding Entrenador in database:")
        for i in range(10):
            print(i+1, end = '\r')
            # try:
            list_entrenador={}
            id = randint(10000000,99999999)
            id = str(id) + random.choice(letras)
            nom = fake.unique.first_name()
            modalidad=1
            if i > 2:
                modalidad = randint(1,3)
            else:
                modalidad = i + 1
            list_entrenador["dni"]=id
            list_entrenador["modalidad"]=modalidad
            lista_entrenadores[i]=list_entrenador
            apellido = fake.unique.last_name()
            fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
            telefono=randint(100000000,999999999)
            direccion=fake.unique.address()
            federacion=randint(10000000000000,99999999999999)
            d = fake.unique.iban()
            IBAN=Compte.objects.create(IBAN=d)
            Entrenador.objects.create(numFederacio=federacion ,compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
        #     # except:
        #     #     pass

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
        print("Adding Horarios in database:")
        for i in range(3000):
            print(i+1, end = '\r')
            date_clase= fake.date_between_dates(date_start=datetime(2012,5,1), date_end=datetime(2022,12,1))
            if date_clase.weekday() < 5:
                try:
                    hora = horas_clase[r(len(horas_clase))]
                    Horari.objects.create(data=date_clase, horario=hora)
                except:
                    pass


        print("Adding Clientes in database:")
        for i in range(400):
            print(i+1, end = '\r')
            # try:
            id = randint(10000000,99999999)
            id = str(id) + random.choice(letras)
            nom = fake.unique.first_name()
            apellido = fake.unique.last_name()
            fecha_nacimiento = fake.date_between_dates(date_start=datetime(1970,1,1), date_end=datetime(2001,12,12))
            telefono=randint(100000000,999999999)
            direccion=fake.unique.address()
            domiciliat=str(choices([0,1], [0.4, 0.6]))
            domiciliat=bool(int(domiciliat[1]))
            IBAN=None
            if domiciliat==True:
                pariente=str(choices([0,1], [0.9, 0.1]))
                pariente=bool(int(pariente[1]))
                if pariente:
                    IBAN=random.choice(Compte.objects.all())
                else:
                    d = fake.unique.iban()
                    IBAN=Compte.objects.create(IBAN=d)
            cliente_obj=Client.objects.create(PagementDomiciliat=domiciliat, compteIBAN=IBAN, DNI=id, nom=nom, cognom=apellido, DataNaix=fecha_nacimiento, Telefon=telefono, direccio=direccion)
            

        # AÑADIMOS UNA INSCRIPCIÓN 
            numero_inscripcion=randint(10000000,99999999)
            tipo=str(choices([1,2,3], [0.8, 0.1, 0.1]))
            fecha_inscripcion = fake.date_between_dates(date_start=datetime(2012,1,1), date_end=datetime.now())
            Inscripcion_obj=Inscripcio.objects.create(numInscripcio=numero_inscripcion,tipus=tipo[1],dataInscripcio=fecha_inscripcion,client=cliente_obj)
            

        # AÑADIMOS HISTORICOS 

            date_type=fecha_inscripcion
            first_month=True
            lo_dejo=False
            pagament_f=50
            if tipo == 2:
                pagament_f=25
            elif tipo == 3:
                pagament_f=40
            while date_type < datetime.now().date() and not lo_dejo:
                HistoricPagaments.objects.create(numInscripcio=Inscripcion_obj, data=date_type, Pagament=pagament_f)
                lo_dejo=str(choices([0,1], [0.9, 0.1]))
                lo_dejo=bool(int(lo_dejo[1]))

                if first_month:
                    date_type=date_type.replace(day=1)
                    first_month=False
                date_type = date_type + relativedelta(months=+1)

            solicitaFederacion=str(choices([0,1], [0.7, 0.3]))
            solicitaFederacion=bool(int(solicitaFederacion[1]))
            if solicitaFederacion:
                numSolFederacio=random.choice(letras)+random.choice(letras)+str(randint(10000000,99999999))
                pagamentF=str(choices([0,1], [0.05, 0.95]))
                pagamentF=bool(int(pagamentF[1]))
                concedidaF=False
                if pagamentF:
                    concedidaF=str(choices([0,1], [0.3, 0.7]))
                    concedidaF=bool(int(concedidaF[1]))
                data=fake.date_between_dates(date_start=fecha_inscripcion, date_end=date_type)
                numero_inscripcion_f=None
                data_final=None
                if concedidaF:
                    numero_inscripcion_f=randint(10000000000000,99999999999999)
                    data_final = data + relativedelta(years=+1)
                SolicitudFederacio.objects.create(numero=numSolFederacio, pagament=pagamentF, concedida=concedidaF, data=data, numFederacio=numero_inscripcion_f, dataCaducitat=data_final, client=cliente_obj)
            
            

        print("Adding Clases in database:")
        for i in range(10000):
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
                entrenador_obj=Entrenador.objects.get(DNI=entrenador["dni"])
                existeix = Classe.objects.filter(coach=entrenador_obj, horari=date_clase)
                if not existeix:
                    if  date_type.weekday() == 3:
                        if  time_type <  datetime.strptime('13:00', '%H:%M').time():
                            tipo=3
                    elif  date_type.weekday() == 4:
                        if  time_type > datetime.strptime('17:00', '%H:%M').time():
                            tipo=3
                    clase_obj=Classe.objects.create(modalitat=model, tipus=tipo, realitzada=valor, coach=entrenador_obj, horari=date_clase)
                    numParticipants=randint(8,25)
                    for _ in range(numParticipants):
                        # try:
                        cliente_obj=random.choice(Client.objects.all())
                        List_inscripcion=cliente_obj.inscripcio_set.all()
                        inscrito=False
                        tipus_insc=2
                        if List_inscripcion:
                            for inscripcion in List_inscripcion:
                                List_Historic=inscripcion.historicpagaments_set.latest('data')
                                primer_historic=inscripcion.historicpagaments_set.first()
                                data_final = List_Historic.data + relativedelta(months=+1)
                                if data_final > date_type and primer_historic.data < date_type:
                                    inscrito=True
                                    tipus_insc=inscripcion.tipus
                        if inscrito==True and tipus_insc!=2:
                            if tipus_insc == 3:
                                if time_type > datetime.strptime('17:00', '%H:%M').time():
                                    pass
                            else:
                                if tipo == 3:
                                    List_solFederacio=cliente_obj.solicitudfederacio_set.all()
                                    if List_solFederacio:
                                        for solFederacio in List_solFederacio:
                                            if solFederacio.concedida and solFederacio.dataCaducitat > date.today():
                                                cliente_obj.classes.add(clase_obj)
                                else:
                                    cliente_obj.classes.add(clase_obj)




                   

        print("Adding Faltas in database:")
        for i in range(30):
            print(i+1, end = '\r')
            try:
                data=fake.date_between_dates(date_start=datetime(2015,1,1), date_end=datetime.now())
                personalF=Personal.objects.first()
                Faltes.objects.create(dataFalta=data, personal=personalF)
            except:
                pass

