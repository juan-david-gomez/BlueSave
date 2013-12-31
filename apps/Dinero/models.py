from django.db import models
import moneyed

class categoria(models.Model):
	nombreCategoria = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombreCategoria

class tipo(models.Model):
	nombreTipo  = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombreTipo

class movimiento(models.Model):
	valor =models.DecimalField( max_digits=5, decimal_places=3)

	Categoria = models.ForeignKey(categoria,default=1)
	anotaciones = models.TextField(default="Sin Anotaciones")
	Tipo = models.ForeignKey(tipo)
	fecha = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		tipo =  str(self.Tipo)
		return tipo

