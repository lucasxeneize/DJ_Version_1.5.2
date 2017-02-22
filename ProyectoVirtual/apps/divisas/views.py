from django.views.generic import CreateView, TemplateView, ListView
from .models import	Cotizacion
from django.core.urlresolvers import reverse_lazy

class InicioCotizacion(ListView):
	template_name = 'divisas/inicio.html'
	model = Cotizacion

class RegistrarCotizacion(CreateView):
	template_name  = 'divisas/registrarCotizacion.html'
	model = Cotizacion
	success_url = reverse_lazy('reportar_cotizacion')


#class ReportarCotizacion(TemplateView):
#	template_name = 'divisas/reportarCotizacion.html'

class ReportarCotizacion(ListView):
	template_name = 'divisas/reportarCotizacion.html'
	model = Cotizacion