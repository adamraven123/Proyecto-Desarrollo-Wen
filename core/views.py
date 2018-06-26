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
		cant = mater.total()
		data = {
			"cant":cant,
			'select':select}
		print ("DATA ", data)
		return JsonResponse(data)
	else:
		material = Material.objects.all()
		stock = Stock.objects.all()
		data["materiales"] = material
	
	data["titulo"] = "Agregar Stock"
	data["tabla"] = "Tabla de Materiales"
	template_name = 'ingresar_stock.html'
	return render(request, template_name, data)

def crearMaterial(request):
	data = {}
	if request.method == "POST":
		medida = request.POST["medida"]
		tipo = request.POST["tipo"]
		nombre = request.POST["nombre"]
		codigo = request.POST["codigo"]
		stock = Stock.objects.create(
			medida = medida,
			cantidad = 0,
			)
		stock.save()
		mater = Material.objects.create(
			cod = medida,
			tipo = tipo,
			nombre = nombre,
			stock= stock,
			)
		mater.save()
		html = "<tr>\
					<td>%s</td>\
					<td>%s</td>\
					<td>%s</td>\
					<td>%s</td>\
		</tr>" %(nombre,codigo,tipo,stock)
		data = {
			"html":html,
		}
	return JsonResponse(data)

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
		data['materiales'] = Material.objects.filter(tipo="MP").all()
		template_name = 'pastel/admin_pastel.html'
		return render(request,template_name,data)

def pedidos(request):
	data = {}
	data['inicio'] = 'Bienvenidos'
	template_name = 'pedi_clie.html'
	return render(request,template_name,data)

def create_base(request):
	name = request.POST['nombre_input']
	n_base = BasePastel.objects.create(
		nombre = name
	)
	n_base.save()
	i = 0
	while i < 200:
		try:
			ing_pk = request.POST['ing_'+str(i)]
			ingrediente = Material.objects.get(pk=ing_pk)
			cantidad = request.POST['cant_'+str(i)]
			receta = CantReceta.objects.create(
				ingrediente = ingrediente,
				cantidad = cantidad
			)
			receta.save()
			n_base.receta.add(receta)
		except IndexError:
			break

	return JsonResponse({"mensaje":"ok"})