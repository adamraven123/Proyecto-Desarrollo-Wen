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
		n_user = User.objects.create_user(
			username=request.POST["rut"],
			password=request.POST["name"].split(" ")[0]+request.POST["dv"],
			email=request.POST['email'],
			first_name=request.POST["name"],
			last_name=request.POST['last_name'],
		)
		n_user.save()
		n_perfil = PerfilUsuario.objects.create(
			user = n_user,
			role = request.POST["tipo"],
			rut = request.POST['rut'],
			dv = request.POST['dv']
		)
		n_perfil.save()
		return JsonResponse({'mensaje':'El usuario ha sido creado con éxito. \n La contraseña es una combinación de su primer y su dígito verificador.'})
	else:
		data['users'] = PerfilUsuario.objects.all()
		template_name = 'perfil_usuario/admin_usuarios.html'
		return render(request,template_name,data)

def pedidos(request):
	data = {}
	data['inicio'] = 'Bienvenidos'
	template_name = 'pedi_clie.html'
	return render(request,template_name,data)

def recibir(request):
    hmtl ='<div class="card-header">Tus elecciones</div><div class="card-body" style="margin-top: -5%;"><div class="dropdown">										<button type="button" class="btn btn-primary dropdown-toggle inter-space" data-toggle="dropdown">¿Para cuantas personas?</button>										<div class="dropdown-menu"><a class="dropdown-item 20" href="">20 personas</a><a class="dropdown-item 30" href="">30 personas</a><a class="dropdown-item 40" href="">40 personas</a></div></div><div class="dropdown"><button type="button" class="btn btn-primary dropdown-toggle inter-space" data-toggle="dropdown">¿Que base le gustaria?</button><div class="dropdown-menu"><a class="dropdown-item" href="">base 1</a><a class="dropdown-item" href="">base 2</a><a class="dropdown-item" href="">base 3</a></div></div><div class="dropdown"><button type="button" class="btn btn-primary dropdown-toggle inter-space" data-toggle="dropdown">Ingrediente 1ra capa </button><div class="dropdown-menu"><a class="dropdown-item" href="">ingrediente 1</a><a class="dropdown-item" href="">ingrediente 2</a><a class="dropdown-item" href="">ingrediente 3</a></div></div><div class="dropdown"><button type="button" class="btn btn-primary dropdown-toggle inter-space" data-toggle="dropdown">Ingrediente 2da capa </button><div class="dropdown-menu"><a class="dropdown-item" href="">ingrediente 1</a><a class="dropdown-item" href="">ingrediente 2</a><a class="dropdown-item" href="">ingrediente 3</a></div></div><div class="dropdown"><button type="button" class="btn btn-primary dropdown-toggle inter-space" data-toggle="dropdown">Ingrediente 3ra capa </button><div class="dropdown-menu"><a class="dropdown-item" href="">ingrediente 1</a><a class="dropdown-item" href="">ingrediente 2</a><a class="dropdown-item" href="">ingrediente 3</a></div></div></div></div>'

    data = {
        "html":hmtl,
    }
    return JsonResponse(data)

