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
		mater.stock.save()
		mater.save()
		select = "#cant_"+str(mater.pk)
		cant = mater.total
		data = {
			"cant":cant,
			'select':select}
		return JsonResponse(data)
	else:
		material = Material.objects.all()
		stock = Stock.objects.all()
		data["materiales"] = material
	
	data["titulo"] = "Agregar Stock"
	data["tabla"] = "Tabla de Materiales"
	template_name = 'ingresar_stock.html'
	return render(request, template_name, data)

def admin_usuario(request):
	data = {}
	if request.method == "POST":
		pass
	else:
		data['users'] = PerfilUsuario.objects.all()
		template_name = 'perfil_usuario/admin_usuarios.html'
		return render(request,template_name,data)
def pedidos(request):
	data = {}
	data['inicio'] = 'Bienvenidos'
	template_name = 'pedi_clie.html'
	return render(request,template_name,data)


