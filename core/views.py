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
		
		if request.POST['tipo'] == "CO":
			if Cliente.objects.filter(mail=request.POST['email']).exists():
				cliente = Cliente.objects.get(email=request.POST['email'])
				cliente.userprofile = n_perfil
				cliente.save()
			else:
				n_cliente = Cliente.objects.create(
					nombre = n_user.first_name,
					apellido = n_user.last_name,
					mail = n_user.email
				)
				n_cliente.save()
		elif request.POST['tipo'] == 'AD':
			n_user.is_staff = True
			n_user.save()
		return JsonResponse({'mensaje':'El usuario ha sido creado con éxito. \n La contraseña es una combinación de su primer y su dígito verificador.'})
	else:
		data['users'] = PerfilUsuario.objects.all()
		template_name = 'perfil_usuario/admin_usuarios.html'
		return render(request,template_name,data)
def admin_pastel(request):
	data = {}
	if request.method == "POST":
		return JsonResponse({'mensaje':'El usuario ha sido creado con éxito. \n La contraseña es una combinación de su primer y su dígito verificador.'})
	else:
		data['pasteles'] = Pastel.objects.all()
		template_name = 'pastel/admin_pastel.html'
		return render(request,template_name,data)

def pedidos(request):
	data = {}
	data['inicio'] = 'Bienvenidos'
	template_name = 'pedi_clie.html'
	return render(request,template_name,data)

