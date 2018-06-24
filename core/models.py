from django.utils import timezone
from datetime import date
from django.db import models
from core.defines import *
from django.contrib.auth.models import User


class Stock(models.Model):
	medida = models.CharField(
				max_length=2,
				choices= MEDIDA_CHOICE,
				default= MEDIDA_DEFAULT
			)
	cantidad = models.IntegerField(default=0)

class Materia(models.Model):
	cod = models.CharField(max_length=250)
	tipo = models.CharField(max_length=2,choices=MATERIA_TIPO_CHOICES,default=MATERIA_TIPO_DEFAULT)
	nombre = models.CharField(max_length=240)
	stock = models.ForeignKey(Stock,on_delete=models.CASCADE, blank = True)
	def __str__(self):
		return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=240)
    apellido = models.CharField(max_length=240)
    rut = models.CharField(max_length=240)
    mail = models.CharField(max_length=240)
    def __str__(self):
        return self.nombre
	
class Pastel(models.Model):
	nombre = models.CharField(max_length=240)
	sabor = models.ManyToManyField(Materia,default=None,blank=True)
	tipo = models.CharField(
			max_length=10,
			choices= TIPO_CHOICE,
			default= TIPO_DEFAULT
	)
	vegano = models.BooleanField(default=False)
	celiaco = models.BooleanField(default=False)
	def __str__(self):
		return self.nombre

class Pedido(models.Model):
	fecha_pedido = models.DateField(default=date.today)
	fecha_entrega = models.DateField()
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, blank = True)
	materia = models.ManyToManyField(Materia,blank = True)
	sabor = models.CharField(
			max_length=10,
			choices= SABOR_CHOICE,
			default= SABOR_DEFAULT
		)
	tipo = models.CharField(
			max_length=10,
			choices= TIPO_CHOICE,
			default= TIPO_DEFAULT
		)
	vegano = models.BooleanField(default=False)
	celiaco = models.BooleanField(default=False)
	
class PerfilUsuario(models.Model):
	user = models.OneToOneField(User,null=True,blank=True,on_delete= models.CASCADE)
	role = models.CharField(max_length=2,choices=TIPO_USUARIO_CHOICES,default=TIPO_USUARIO_DEFAULT)
	rut = models.IntegerField()
	dv = models.CharField(max_length=1, default="")
	fecha_creacion = models.DateTimeField(default=timezone.now)
