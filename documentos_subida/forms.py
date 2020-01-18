from django import forms
from . import models

import datetime

class SubirArchivo(forms.Form):
    nombre = forms.CharField(label="Titulo:",max_length=60)
    archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    tipos = models.Tipo.objects.all()
    opciones_tipo = []
    for tipo in tipos:
        opciones_tipo.append((tipo.descripcion,tipo.descripcion))
    #print(opciones_tipo)
    tipo = forms.ChoiceField(label="Tipo:",choices=opciones_tipo)

    ramos = models.Asignatura.objects.all()
    opciones_ramo = []
    for ramo in ramos:
        opciones_ramo.append((ramo.codigo, ramo.nombre + " ( " + str(ramo.codigo) + " ) " ))
    #print(opciones_ramo)
    ramo = forms.MultipleChoiceField(label="Ramos:", choices=opciones_ramo, help_text="utiliza ctrl + click para seleccionar varios")

    fecha_conocida = forms.BooleanField(label="Fecha del documento conocida",initial=True,required=False)

    ano_actual = datetime.datetime.now().year
    ano = forms.DecimalField(label="Año", initial=ano_actual, min_value=2000, max_value=ano_actual)
    semestre = forms.DecimalField(label="Semestre", initial=1, min_value=1, max_value=2)
