from django.contrib import admin
from django import forms
from .models import Stock, Material, Cliente, Pastel, CantReceta, BasePastel, Pedido, CapaPastel, PerfilUsuario

class StockAdminForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class StockAdmin(admin.ModelAdmin):
    form = StockAdminForm
    list_display = ['cantidad']

admin.site.register(Stock, StockAdmin)


class MaterialAdminForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = '__all__'


class MaterialAdmin(admin.ModelAdmin):
    form = MaterialAdminForm
    list_display = ['tipo', 'nombre']

admin.site.register(Material, MaterialAdmin)


class ClienteAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ['nombre', 'apellido', 'mail']

admin.site.register(Cliente, ClienteAdmin)


class PastelAdminForm(forms.ModelForm):

    class Meta:
        model = Pastel
        fields = '__all__'


class PastelAdmin(admin.ModelAdmin):
    form = PastelAdminForm
    list_display = ['nombre', 'vegano', 'celiaco']

admin.site.register(Pastel, PastelAdmin)


class CantRecetaAdminForm(forms.ModelForm):

    class Meta:
        model = CantReceta
        fields = '__all__'


class CantRecetaAdmin(admin.ModelAdmin):
    form = CantRecetaAdminForm
    list_display = ['cantidad_total']

admin.site.register(CantReceta, CantRecetaAdmin)


class BasePastelAdminForm(forms.ModelForm):

    class Meta:
        model = BasePastel
        fields = '__all__'


class BasePastelAdmin(admin.ModelAdmin):
    form = BasePastelAdminForm
    list_display = ['nombre']

admin.site.register(BasePastel, BasePastelAdmin)


class PedidoAdminForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoAdmin(admin.ModelAdmin):
    form = PedidoAdminForm
    list_display = ['fecha_pedido', 'fecha_entrega', 'personas', 'vegano', 'celiaco']

admin.site.register(Pedido, PedidoAdmin)


class CapaPastelAdminForm(forms.ModelForm):

    class Meta:
        model = CapaPastel
        fields = '__all__'


class CapaPastelAdmin(admin.ModelAdmin):
    form = CapaPastelAdminForm
    list_display = ['crema']

admin.site.register(CapaPastel, CapaPastelAdmin)


class PerfilUsuarioAdminForm(forms.ModelForm):

    class Meta:
        model = PerfilUsuario
        fields = '__all__'


class PerfilUsuarioAdmin(admin.ModelAdmin):
    form = PerfilUsuarioAdminForm
    list_display = ['role', 'rut', 'dv', 'fecha_creacion']

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)

