from django.urls import path
from AppProductos import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("fotolibros/", views.fotolibros, name="fotolibros"),
    path("copiasImpresas/", views.copiasImpresas, name="copias"),
    path(
        "sesionesFotograficas/", views.sesionesFotograficas, name="sesionesFotograficas"
    ),
    path("sesionesFormulario/", views.sesionesFormulario, name="sesionesFormulario"),
    path(
        "fotolibrosFormulario/", views.fotolibrosFormulario, name="fotolibrosFormulario"
    ),
    path("copiasFormulario/", views.copiasFormulario, name="copiasFormulario"),
    path("busquedaSesiones/", views.busquedaSesiones, name="busquedaSesiones"),
    path("buscar/", views.buscar, name="buscar"),
]
