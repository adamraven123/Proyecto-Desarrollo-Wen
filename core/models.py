from django.utils import timezone
from datetime import date
from django.db import models

SABOR_CHOICE = (
  ('Choc', 'Chocolate'),
  ('Mnj', 'Manjar'),
  ('Ntl', 'Nutella'),
  ('S.N','Selva negra'),
  ('C.P','Crema-Pastelera'),
  ('3L','3Leches'),
  ('M.L','Merengue/Lucuma'),
)

TIPO_CHOICE = (
  ('M.H', 'Millhojas'),
  ('Bzch', 'Bizcocho'),
  ('Ygt', 'Yogurt'),
  ('Pqq','Panqueque'),
  ('H.ca','Hojarasca'),
  ('Hlds','Heladas'),
  ('Mrg','Merengue'),
)

MEDIDA_CHOICE = (
	('Gr','Gramos'),
	('Cc', 'Centimetro cubico'),
	)

SABOR_DEFAULT = 'S.N'
TIPO_DEFAULT = 'Bzch'
MEDIDA_DEFAULT = 'Gr'


class Stock(models.Model):
	medida = models.CharField(
				max_length=12,
				choices= MEDIDA_CHOICE,
				default= MEDIDA_DEFAULT
			)
	cantidad =models.IntegerField()

class Materia(models.Model):
	cod = models.IntegerField()
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
	
class Pasteles(models.Model):
	nombre = models.CharField(max_length=240)
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
	
