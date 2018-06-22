from django.shortcuts import render
from core.models import *
# Create your views here.

def index(request):
	data = {}
	data['inicio'] = 'Bienvenidos'
	template_name = 'index.html'
	return render(request,template_name,data)
