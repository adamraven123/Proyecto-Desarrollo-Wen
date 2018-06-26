from django.shortcuts import render
from core.models import *
from django.http import JsonResponse
from .forms import MaterialForm
# Create your views here.

def index(request):
	data = {}
	data['inicio'] = 'Bienvenidos'
	template_name = 'index.html'
	return render(request,template_name,data)

def ingresar_stock(request):
	data = {}
	if request.method == "POST":
		mater = request.POST["material"]
		cantidad = request.POST["cantidad"]
		mater = Material.objects.get(pk=int(mater))
		print (mater.nombre)
		mater.stock.cantidad += int(cantidad)
		print (mater.stock.cantidad)
		mater.save()
		#print (cantidad)
	else:
		material = Material.objects.all()
		stock = Stock.objects.filter()
		data["materiales"] = material
	
	data["titulo"] = "Agregar "
	template_name = 'ingresar_stock.html'
	return render(request, template_name, data)

