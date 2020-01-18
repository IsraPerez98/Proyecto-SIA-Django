from django.db import models

from django.db.models import signals
from django.dispatch import receiver
import os
from django.conf import settings

# Create your models here.

class Asignatura(models.Model): #los documentos pertenecientes al ramo
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre + " (" + self.codigo + ")" 



class Tipo(models.Model): #el tipo de documeto
    descripcion = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.descripcion


class Semestre(models.Model): # el semestre de el documento
    ano = models.IntegerField()
    semestre = models.BooleanField()
    #0 = semestre 1
    #1 = semestre 2

    def __str__(self):
        return "Semestre: " + str(int(self.semestre) + 1) + "   Año: " + str(self.ano)

def directorio_subida(instance, filename):
    return "docs/" + instance.asignatura_principal.codigo + "/" + instance.fecha_subida.strftime("%d%m%Y_%H_%M_%S") + "_" + filename

class Documento(models.Model):
    tipo = models.ForeignKey(Tipo,on_delete=models.PROTECT)
    disponible = models.BooleanField(default=False) # este lo cambia el admin
    nombre = models.CharField(max_length=60)
    semestre = models.ForeignKey(Semestre,on_delete=models.PROTECT, null=True)
    fecha_subida = models.DateTimeField(auto_now=True)

    #aunque usemos el modelo "EnlaceAsignatura" tenemos que fijar una asignatura principal
    #para poder usar la asignatura en la ubicacion de subida
    asignatura_principal = models.ForeignKey(Asignatura,on_delete=models.PROTECT)

    archivo = models.FileField(upload_to=directorio_subida, unique=True)
    usuario = models.ForeignKey("registro.Usuario", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre + " (" + str(self.archivo) + ")"

@receiver(signals.post_delete, sender=Documento)
def eliminar_archivo(sender, instance, **kwargs):
    """
    Con esto eliminamos el archivo correspondiente
    cuando el "Documento" sea eliminado
    """
    if instance.archivo:
        if os.path.isfile(instance.archivo.path):
            print("Eliminando ",instance.archivo.path)
            os.remove(instance.archivo.path)



class EnlaceAsignatura(models.Model): #para enlazar un documento con n asignaturas (puede ser misma asignatura con distinto codigo, para no repetir archivo)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return "doc: " + str(self.documento) + "   asignatura: " + str(self.asignatura)