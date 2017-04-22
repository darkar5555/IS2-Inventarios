from django.contrib import admin

from .models import Usuario
from .models import Proveedor
from .models import Almacen
from .models import Clasificacion
from .models import Grupo

class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "contrasena", "email"]

	class Meta:
		model = Usuario

admin.site.register(Usuario, AdminUsuario)

class AdminProveedor(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "telefono","direccion","email"]

	class Meta:
		model = Proveedor

admin.site.register(Proveedor,AdminProveedor)

class AdminAlmacen(admin.ModelAdmin):
	list_display = ["__str__", "anaqueles_por_fila", "direccion", "filas"]

	class Meta:
		model = Almacen

admin.site.register(Almacen,AdminAlmacen)

class AdminClasificacion(admin.ModelAdmin):
	list_display = ["__str__", "nombre", "descripcion"]
	
	class Meta:
		model = Clasificacion

admin.site.register(Clasificacion,AdminClasificacion)

class AdminGrupo(admin.ModelAdmin):
	list_display = ["__str__", "nombre_grupo", "nombre_subgrupo"]

	class Metal:
		model = Grupo

admin.site.register(Grupo,AdminGrupo)
