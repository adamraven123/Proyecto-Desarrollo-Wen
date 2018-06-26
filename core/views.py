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
		data['form'] = MaterialForm(request.POST)
		if data['form'].is_valid():
			data ['form'].save()
	else:
		data['form'] = MaterialForm()
	template_name = 'ingresar_stock.html'
	return render(request,template_name,data)

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

