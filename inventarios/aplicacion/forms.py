from django import forms

class IniciarSesionForm(forms.Form):
	nombre_form = forms.CharField(max_length = 20)
	contrasena_form = forms.CharField(max_length = 20)


class RegistrarUsuarioForm(forms.Form):
	nombre_form=forms.CharField(max_length=20)
	contrasena_form=forms.CharField(max_length=20)
	email_form=forms.EmailField()
