from django.shortcuts import render

from . import models
from .forms import SubirArchivo
import datetime
# Create your views here.

def subir(response):
    if response.method == "POST":
        form = SubirArchivo(response.POST, response.FILES)
        if form.is_valid():
            
            tipo = form.cleaned_data["tipo"]
            nombre = form.cleaned_data["nombre"]
            fecha_conocida = form.cleaned_data["fecha_conocida"]
            if fecha_conocida:
                ano = form.cleaned_data["ano"]
                semestre = form.cleaned_data["semestre"]
            ramos = form.cleaned_data["ramo"]
            usuario = response.user

            d = models.Documento(archivo=response.FILES["archivo"])
            d.tipo = models.Tipo.objects.get(descripcion=tipo)
            d.disponible = False
            d.nombre = nombre
            if fecha_conocida:
                sem_bool = (semestre == 2)
                d.semestre, semestre_nuevo_creado = models.Semestre.objects.get_or_create(ano=ano, semestre=sem_bool)
            d.fecha_subida = datetime.datetime.now()
            d.asignatura_principal = models.Asignatura.objects.get(codigo=ramos[0])
            d.usuario = usuario
            d.save()
            print("NUEVO DOCUMENTO")
            print(d)
            print("ENLAZADO A:")
            for ramo in ramos:
                #enlazamos a todas las asignaturas que corresponden
                print(ramo,end="")
                enlace = models.EnlaceAsignatura()
                enlace.documento = d
                enlace.asignatura = models.Asignatura.objects.get(codigo=ramo)
                enlace.save()
            return render(response, 'documentos_subida/exito.html')
                
            
    else:
        form = SubirArchivo()
    return render(response, 'documentos_subida/subida.html', {"form":form})