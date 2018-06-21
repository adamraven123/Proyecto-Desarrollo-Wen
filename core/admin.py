from django.contrib import admin

from .models import *

admin.site.register(Stock)
admin.site.register(Material)
admin.site.register(Cliente)
admin.site.register(Pastel)
admin.site.register(Pedido)