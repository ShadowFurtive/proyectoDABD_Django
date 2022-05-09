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
        # return self.DNI, self.nom, self.cognom, self.DataNaix, self.Telefon, self.direccio


class Client(models.Model):
    template = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    PagementDomiciliat = models.BooleanField()

    def __str__(self):
        return '[ Pagament domiciliat: {} ] , {} , {} , {} , {} , {} , {}'.format(self.PagementDomiciliat, self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio)
        # return '[ Pagament domiciliat: ' + str(self.PagementDomiciliat) + '] ', self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio

class Personal(models.Model):
    template = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return '{} , {} , {} , {} , {} , {}'.format(self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio)
        # return self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio

class Entrenador(models.Model):
    template = models.ForeignKey(PersonaTemplate, on_delete=models.CASCADE)
    NumFederacio = models.IntegerField(validators=[MaxValueValidator(99999999999999)])

    def __str__(self):
        return '{} , {} , {} , {} , {} , {} , {}'.format(self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio, str(self.NumFederacio))
        #return self.template.DNI, self.template.nom, self.template.cognom, self.template.DataNaix, self.template.Telefon, self.template.direccio, str(self.NumFederacio)
