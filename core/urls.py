from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
	path('',views.index, name = "index"),
	path('add_stock/',views.ingresar_stock, name = "add_stock"),
	path('add_material/',views.crearMaterial, name = "add_material"),
	path('admin_usuario/',views.admin_usuario, name = "admin_usuario"),
	path('pedidos/',views.pedidos, name = "pedidos"),
]
