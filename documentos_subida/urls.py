from django.urls import path

from . import views

urlpatterns = [
    path("", views.subir, name="documentos_subida"),
]
