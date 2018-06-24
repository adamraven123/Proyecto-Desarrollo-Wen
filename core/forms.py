from django import forms
from .models import Stock, Material, Cliente, Pastel, CantReceta, BasePastel, Pedido, CapaPastel, PerfilUsuario


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['cantidad']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['cod', 'tipo', 'nombre', 'stock']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'rut', 'mail']


class PastelForm(forms.ModelForm):
    class Meta:
        model = Pastel
        fields = ['nombre', 'vegano', 'celiaco', 'capas', 'base']


class CantRecetaForm(forms.ModelForm):
    class Meta:
        model = CantReceta
        fields = ['medida', 'ingrediente']


class BasePastelForm(forms.ModelForm):
    class Meta:
        model = BasePastel
        fields = ['nombre', 'receta']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'fecha_entrega', 'personas', 'vegano', 'celiaco', 'cliente', 'capas', 'base']


class CapaPastelForm(forms.ModelForm):
    class Meta:
        model = CapaPastel
        fields = ['crema', 'pastel', 'ingredientes']


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['role', 'rut', 'dv',]


