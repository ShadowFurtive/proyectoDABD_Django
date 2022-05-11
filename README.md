# PROYECTO FINAL DE DABD
## _PROGRAMA DE GESTIÓN DE UN CLUB DE LUCHA_

[![N|Solid](https://www.upc.edu/comunicacio/ca/identitat/descarrega-arxius-grafics/fitxers-marca-principal/upc-positiu-p3005.png)](https://www.epsevg.upc.edu/ca/escola)

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Proyecto final de la asignatura de DABD, EPSEVG-UPC.

- Autor: Mario Kochan
- Fecha: 12/06/2022
- Profesor: Jordi Estve

## Características

- Proyecto realizado con [Django]
- Uso de [GITHUB]
- Modelación en UML del proyecto
- Uso de [Faker] para generar datos falsos
- Uso de terminal Windows Powershell
- Creación del .md con [Dillinger](https://dillinger.io/)


## Despliegue y uso de Django

### Instalación

Para el proyecto vamos a desplegar un entorno virtual [Virtualenv](https://docs.python.org/es/3/library/venv.html).

Trabajaremos sobre Windows Powershell:

```sh
pip install virtualenv
python -m venv django
Set-ExecutionPolicy Unrestricted -Scope Process
cd django
Scripts/activate
Scripts/Activate.ps1
Set-ExecutionPolicy Default -Scope Process
```

Creamos el proyecto [Django]:

```sh
pip install Django
django-admin startproject dabd
python manage.py startapp club
```
Y empezamos a trabajar :)

Puede ser que sea necesario crear un super user para la página administrativa de [Django]:
```sh
python manage.py createsuperuser
```

### Ejecutar Django

Migramos los elementos en el Django

```sh
python manage.py makemigrations
python manage.py migrate
```

Y ejecutamos de forma local la página

```sh
python manage.py runserver 8080
```

### Generación de FakeData

Podemos ejecutar un comando junto con manage.py para generar los datos falsos:

```sh
python manage.py createdata
```
[Video](https://www.youtube.com/watch?v=8LHdbaV7Dvo) en el que me he basado para hacer el comando.

## ANEXO

### Enunciado (En catalán)

La garra és un club de lluita i un gimnàs que imparteix classes de diferents formes de lluita i on també es pot entrenar amb manuelles. Amb el temps, s'han inscrit moltes persones i ara es necessita actualitzar el seu sistema Excel a mà a un sistema més avançat que permeti controlar els clients.

El club sols obre de dilluns a divendres.

Els horaris d'obertura són els següents: cada dia (de dilluns a divendres), de 10 fins a les 13. I després de 17 fins a les 21:30.

Les modalitats de lluita disponibles són: boxa, Muay Thai, MMA.

En la garra hi ha els entrenadors que són els responsables de realitzar les classes i el personal del club, que s'encarrega de netejar el club, el gimnàs i de resoldre qüestions.

Dels entrenadors, volem saber: DNI, nom i cognom, data de naixement, número de la federació (valor únic de 12 dígits), número del telèfon, direcció actual, número del compte bancari (IBAN).

Per cada entrenador volem saber quines classes imparteix: si boxa, thai, MMA... quins dies de la setmana fa classes i quines hores. Però, pot sorgir que cert dia un entrenador no pugui impartir classe, per tant, s'ha de saber quins dies ha faltat, ja que no es pot pagar a l'entrenador aquells dies que no hagi fet classes.

Les classes es distingeixen per l'hora, dia i qui la fa i estaria bé saber de què serà la classe (boxa, thai o MMA) i que tipus és (si física, si tècnica o contacte).

Del personal del club, sols volem saber: DNI, nom i cognom, data de naixement, número del telèfon, direcció actual, número del compte bancari (IBAN). Del personal del club volem saber quins dies ha faltat de la setmana. El personal del club és una persona que assisteix de 10:00 fins a les 13 i de 17 fins a les 21:30 i és la mateixa persona per a tots els dies que està obert el gimnàs.

Per els IBANs dels entrenadors i personals pot ocórrer que hi hagi personal de la familia inscrits al club, i per tant, l'IBAN es repeteixi. 

Ho volem saber tot a la setmana, ja que paguem al personal i als entrenadors el divendres de cada setmana.

Per l'altra banda, tenim els socis, que són els clients que s'inscriuen mitjançant una mensualitat.

La inscripció al club és sempre mitjançant un pagament mensual. Aquest pagament es pot diversificar en diverses formes:

- Inscripció completa: 50 € al mes, pot fer ús del gimnàs i anar a qualsevol classe tant al matí com a la tarda (Boxing, MMA, Thai...)

- Inscripció sols als matins: 40€ al mes, pot fer ús del gimnàs i anar a qualsevol classe però sols als matins.

- Inscripció fitness: Sols pot fer ús del gimnàs sense poder anar a classe de lluita.

De les inscripcions volem saber: el número d'inscripció (valor únic de 8 dígits) i el tipus d'inscripció (fitness, matins o complet) i quan es va realitzar la inscripció.

Dels clients volem saber: DNI, nom i cognom, data de naixement, si estan federats o no estan federats i en cas que estiguin federats, el seu número de federació ( valor únic de 12 dígits) (la federació com tal és una mútua mèdica, per tant, una federació serveix per a totes les modalitats), número de telèfon, direcció actual, si el pagament és domiciliat o no i en cas que sigui domiciliat, el seu IBAN. Pot ocórrer que hi hagi clients amb el mateix IBAN, ja que són parella o família.

Els clients han d'indicar a quins dies i hores participaran en les classes per tal de saber per endavant quantes persones són a classe i així saber com dur a terme les classes.

Tots els clients es poden federar. Poden presentar una sol·licitud juntament amb un pagament. De la federació volem saber: el número identificatiu de la sol·licitud (valor únic de 2 caràcters+8 dígits), si ha pagat o no i s'hi ha sigut concedida.

Clarament, si una persona ja està federat no ha de poder federar-se. I una persona a la qual se l'ha concedit la federació, ha de tenir un número de federació assignat.
També, el dia que se'l va concedir la federació, se li assigna una data de caducitat de la federació, que caducarà fins dintre d'un any.

És important saber si un client ha pagat o no ha pagat el mes corresponent, ja que si no ha pagat no pot accedir a les instal·lacions. Els pagaments els volem guardar per al primer dia de cada mes amb el seu respectiu any.

A més, depenent del tipus d'inscripció que hi ha, pot o no pot assistir a una classe.

Hi ha dies a la setmana que són especials (dijous tarda i divendres al matí) perquè aquells dies són dies de contacte. Per participar en aquells dies, els clients han d'estar federats.

Per identificar als entrenadors, al personal i als clients es farà ús del DNI.
Per identificar les inscripcions es farà ús del codi del número d'inscripció.
Per identificar les sol·licituds de federat es farà ús del número de la sol·licitud.

Pot ocórrer que un client es desapunti i s'apunti passat uns mesos. Ens interessa no eliminar la informació que hi hagi d'ell.

### UML 

![N|Solid](https://lh3.googleusercontent.com/C9RA36Il2l0JfTSggcXT1Qk52Hrw0qd0ZUStqQBVHRLmPEUwl31x3TgQ3Hck-t9Edv0A1FtaEtikuyoGgUqFH-C8hhoemH-LVFUx4vFdVcGrSHg1Vs-2xaGdIjW-BRu9LCvLqo1EXu0p7q1bYEHLWH7YzhOyNCOO7Ml3Yx3UCUGAXpM2HFoxWTrvv4h6sb9w-ilqlIPJ3qXnIVDQytmU31h9mebKF8l5sGrX0lqqS45hkCYx9grFY32cg_kXbhvckdCThZd3pX-Kznh6lZuHzbOg93_X6wpyBirwAWa7ZYxCGMNGlGgbyoWJME5PfGsG9Mhms0YZbWL5j1-uyyNkq51z6xKHLayO6DbPDFNeXmRhP5y6I8Px9tuynp1o9vaRAPqaQDZFPjV7r_9sSUFCzdvKrDPZzbstrCnNGb3hrrV9ENS7KB_rgpDJTSywZ8i2jLGHmr0A9QWQORG3aOzfwbHojQ0q-U7e2mhpb40nJGlCHdHkHHmDjpeeVx9Hp_1XoOOAovgdJVxjkMdzaPmv3Sk4oyApoj1pPa8rxqXjG_ZMii1orPFWFU-gzhRHgHHl_nqV28H6Asm66fpLFiPrfW7mn_0GJIXxW0pppOMBIY8C85fyp5M7blM81h93CktPnqLsrrWJkoZJVyfyMP-SRy-BQSfQYz1zh10nD4vl26FJnA4mPj44F2LS3Vmn4V1100uAziHQYbW7bfGDjjAu76J-IuBW-uaD1mxOe4fRp0d2EXf-chh3oHGMzuH72_Xpw9eviDfBKhPDO3hr8pKZt1LvnzIUgNIoaM_0-9VTnFG7a_nE9zFDAF2yjYf1kdGFN_cMZiOL-yKlKa6vlzxBVMogLZtjEY88IxsADEhCog=w460-h578-no?authuser=0)

   [GITHUB]: <https://github.com/>
   [Django]: <https://www.djangoproject.com/>
   [Faker]: <https://faker.readthedocs.io/en/master/>

