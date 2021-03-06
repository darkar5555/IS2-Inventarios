from django.contrib import admin

from .models import *

class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "contrasena", "email"]

	class Meta:
		model = Usuario

admin.site.register(Usuario, AdminUsuario)

class AdminProveedor(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "telefono","direccion","email"]

	class Meta:
		model = Proveedor

admin.site.register(Proveedor, AdminProveedor)

class AdminAlmacen(admin.ModelAdmin):
	list_display = ["__str__", "anaqueles_por_fila", "direccion", "filas"]

	class Meta:
		model = Almacen

admin.site.register(Almacen, AdminAlmacen)

class AdminPedido(admin.ModelAdmin):
	list_display = ["__str__", "proveedor", "fechaRealizada", "fechaPrevista", "fechaRecibida", "cantidad"]

	class Meta:
		model = Pedido

admin.site.register(Pedido, AdminPedido)
