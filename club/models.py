from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class PersonaTemplate(models.Model):
    DNI = models.CharField(max_length=8)
    nom = models.CharField(max_length=30)
    cognom = models.CharField(max_length=30)
    DataNaix = models.DateField()
    Telefon = models.CharField(max_length=9)
    direccio = models.CharField(max_length=50)

    def __str__(self):
        return '{} , {} , {} , {} , {} , {}'.format(self.DNI, self.nom, self.cognom, self.DataNaix, self.Telefon, self.direccio)

class Compte(models.Model):
    IBAN = models.CharField(primary_key=True, max_length=34)
    def __str__(self):
        return '{} , {} , IBAN: {} '.format(self.dueño.DNI, self.dueño.nom, self.IBAN)

class Client(models.Model):
    template = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    PagementDomiciliat = models.BooleanField()
    compteIBAN = models.ForeignKey(Compte, on_delete=models.CASCADE)

    def __str__(self):
        return '[ Pagament domiciliat: {} ] , {} , {} , {} , {} , {} , {} , {}'.format(self.PagementDomiciliat, self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio, self.compteIBAN)

class Personal(models.Model):
    template = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    compteIBAN = models.ForeignKey(Compte, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} , {} , {} , {} , {} , {}, {}'.format(self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio, self.compteIBAN)

class Inscripcio(models.Model):
    numInscripcio = models.IntegerField(validators=[MaxValueValidator(99999999999999)], primary_key=True)
    tipus = models.PositiveSmallIntegerField(
    choices=(
        (1, "Complet"),
        (2, "Fitness"),
        (3, "Matins"),
    ))
    dataInscripcio = models.DateField()
    client = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    def __str__(self):
        return '{} , {} , {} , {}'.format(self.numInscripcio, self.tipus, self.dataInscripcio, self.client.nom)



class Entrenador(models.Model):
    template = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    numFederacio = models.IntegerField(validators=[MaxValueValidator(99999999999999)], unique=True)
    compteIBAN = models.ForeignKey(Compte, on_delete=models.CASCADE)

    def __str__(self):
        return '{} , {} , {} , {} , {} , {} , {}, {}'.format(self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio, str(self.numFederacio), self.compteIBAN)

class SolicitudFederacio(models.Model):
    numero = models.CharField(max_length=10, primary_key=True)
    pagament = models.BooleanField()
    concedida = models.BooleanField()
    data = models.DateField()
    numFederacio = models.IntegerField(validators=[MaxValueValidator(99999999999999)], blank=True, null=True, unique=True)
    dataCaducitat = models.DateField(blank=True, null=True)
    client = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    def __str__(self):
        return '{} , {} , {} , {} , {} , {} , {}'.format(self.numero, self.pagament, self.concedida, self.data, self.numFederacio, self.dataCaducitat, self.client.nom)
