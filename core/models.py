from django.utils import timezone
from datetime import date
from django.db import models
from core.defines import *
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError

class Stock(models.Model):
	medida = models.CharField(
				max_length=2,
				choices= MEDIDA_CHOICE,
				default= MEDIDA_DEFAULT
			)
	cantidad = models.IntegerField(default=0)
	def __str__(self):
		return str(self.cantidad) + " " + self.medida 

class Material(models.Model):
	cod = models.CharField(max_length=250)
	tipo = models.CharField(max_length=2,choices=MATERIA_TIPO_CHOICES,default=MATERIA_TIPO_DEFAULT)
	nombre = models.CharField(max_length=240)
	stock = models.OneToOneField(Stock,on_delete=models.CASCADE, blank = True)
	def __str__(self):
		return self.nombre
		
	def total(self):
		return '{} {}' . format(self.stock.cantidad, self.stock.medida)

class Cliente(models.Model):
	userprofile = models.ForeignKey('PerfilUsuario',null=True,default=None,on_delete=models.SET_NULL)
	nombre = models.CharField(max_length=240)
	apellido = models.CharField(max_length=240)
	rut = models.CharField(max_length=240)
	mail = models.CharField(max_length=240)
	def __str__(self):
		return self.nombre
	
class Pastel(models.Model):
	nombre = models.CharField(max_length=240)
	cover = models.CharField(
		max_length=2,
		choices=COVER_CHOICE,
		default=COVER_DEFAULT
	)
	capas = models.ManyToManyField("CapaPastel",related_name="capas_pastel",blank=True)
	base = models.ForeignKey("BasePastel",null=True,default=None,on_delete=models.CASCADE)
	vegano = models.BooleanField(default=False)
	image = models.ImageField(upload_to='pasteles',default=None)
	celiaco = models.BooleanField(default=False)
	def __str__(self):
		return self.nombre


class CantReceta(models.Model):
	ingrediente = models.ForeignKey(Material,null=True,on_delete=models.SET_NULL)
	medida = models.CharField(
				max_length=2,
				choices=MEDIDA_CHOICE,
				default=MEDIDA_DEFAULT
			)
	cantidad = models.IntegerField(default=0)
	
	def cantidad_total(self):
		return '{} {}'.format(self.cantidad, self.medida)

class BasePastel(models.Model):
	nombre = models.CharField(max_length=500,null=True,blank=True)
	receta = models.ManyToManyField(CantReceta,blank=True)

class Pedido(models.Model):
	fecha_pedido = models.DateField(default=date.today)
	fecha_entrega = models.DateField()
	cover = models.CharField(
			max_length=2,
			choices=COVER_CHOICE,
			default=COVER_DEFAULT
		)	
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, blank = True)
	personas = models.IntegerField(default=20)
	capas = models.ForeignKey("CapaPastel",null=True,default=None,on_delete=models.CASCADE)
	base = models.ForeignKey(BasePastel,null=True,default=None,on_delete=models.CASCADE)
	vegano = models.BooleanField(default=False)
	celiaco = models.BooleanField(default=False)

class CapaPastel(models.Model):
	crema = models.CharField(max_length=2,choices=CREMA_CHOICES,default=CREMA_DEFAULT)
	ingredientes = models.ManyToManyField(Material,blank=True)

class PerfilUsuario(models.Model):

	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
	role = models.CharField(max_length=2,choices=TIPO_USUARIO_CHOICES,default=TIPO_USUARIO_DEFAULT)
	rut = models.IntegerField()
	dv = models.CharField(max_length=1,default="")
	fecha_creacion = models.DateTimeField(default=timezone.now)

def regions_changed(sender, **kwargs):
    if kwargs['instance'].ingredientes.count() > 3:
        raise ValidationError("You can't assign more than three regions")


m2m_changed.connect(regions_changed, sender=CapaPastel.ingredientes.through)
