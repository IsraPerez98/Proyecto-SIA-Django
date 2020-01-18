from django.shortcuts import render

from django.http import HttpResponse, Http404, StreamingHttpResponse
# Create your views here.
from django.contrib.auth.models import Group

from documentos_subida import models
from django.conf import settings
import os

def index(response): #pagina que muestra los ramos registrados
    ramos = models.Asignatura.objects.all()
    #print(ramos)
    #tambien queremos mostrar cuando documentos tiene cada ramo
    for ramo in ramos:
        ramo.cant_documentos = models.EnlaceAsignatura.objects.filter(asignatura = ramo, documento__disponible = True).count()
    return render(response,"documentos_descarga/indice_principal.html", {"ramos":ramos})

def index_ramo(response,ramo):
    nombre_ramo = models.Asignatura.objects.get(codigo=ramo)
    tipos_de_documentos = models.Tipo.objects.all()
    #print(tipos_de_documentos)
    enlace_documentos = models.EnlaceAsignatura.objects.filter(asignatura=ramo, documento__disponible = True)

    return render(response,"documentos_descarga/indice_ramo.html", {"nombre_ramo":nombre_ramo,"tipos_de_documentos":tipos_de_documentos,"documentos":enlace_documentos})


def descarga_archivo(response,archivo):
    print("intentando bajar " + archivo)
    print(os.path.join(settings.MEDIA_URL,archivo))
    doc = models.Documento.objects.get(archivo=archivo)
    if not doc: #no existe
        raise Http404
    if not doc.disponible: #si no esta disponible solo los admins pueden acceder al doc
        if not response.user.is_authenticated or not response.user.groups.filter(name = "Admin Documentos").exists():
            raise Http404
    try:
        response = StreamingHttpResponse(open(os.path.join(settings.MEDIA_ROOT,archivo), 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(archivo)
        return response
    except Exception:
        raise Http404