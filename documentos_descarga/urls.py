from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="documentos"),
    #path(r'^descarga/(?P<archivo>.*)/$', views.descarga_archivo, name="descarga"),
    path("descarga/<path:archivo>", views.descarga_archivo, name="descarga"),
    path("<slug:ramo>/", views.index_ramo, name="ramo")
]
