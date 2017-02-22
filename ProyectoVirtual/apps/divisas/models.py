from django.db import models

class Cotizacion(models.Model):
	fecha = models.DateField('date published')
	valor = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return str(self.fecha) + " - TC $ " + str(self.valor) + ".-"
