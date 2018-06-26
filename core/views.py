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