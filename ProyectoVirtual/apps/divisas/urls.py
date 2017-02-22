from django.conf.urls import patterns, include, url
from .views import RegistrarCotizacion, ReportarCotizacion, InicioCotizacion

urlpatterns = patterns('',

    url(r'^registrar/', RegistrarCotizacion.as_view(), name="registrar_cotizacion"),
    url(r'^reportar/', ReportarCotizacion.as_view(), name="reportar_cotizacion"),
    url(r'^inicio/', InicioCotizacion.as_view(), name="inicio_divisas"),
)
