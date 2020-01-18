from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Documento)
admin.site.register(models.Asignatura)
admin.site.register(models.Tipo)
admin.site.register(models.Semestre)
admin.site.register(models.EnlaceAsignatura)