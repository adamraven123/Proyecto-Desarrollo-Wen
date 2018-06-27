from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
	path('',views.index, name = "index"),
	path('add_stock/',views.ingresar_stock, name = "add_stock"),
	path('add_material/',views.crearMaterial, name = "add_material"),
	path('admin_usuario/',views.admin_usuario, name = "admin_usuario"),
	path('admin_pastel/',views.admin_pastel, name = "admin_pastel"),
	path('pedidos/',views.pedidos, name = "pedidos"),
	path('create_base/',views.create_base, name = "create_base"),
	path('create_pastel/',views.create_pastel, name = "create_pastel"),
]
