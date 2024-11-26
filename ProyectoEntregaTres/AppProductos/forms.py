from django import forms


class SesionFormulario(forms.Form):
    """Formulario para ingresar datos de sesiones fotograficas"""

    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=100)
    precio = forms.IntegerField()


class CopiaFormulario(forms.Form):
    """Formulario para ingresar datos de copias impresas de fotografias"""

    superficie = forms.CharField(max_length=40)
    tamanio = forms.IntegerField()
    precio = forms.IntegerField()


class FotolibroFormulario(forms.Form):
    """Formulario para ingresar datos de fotolibros artesanales"""

    tamanio = forms.IntegerField()
    cant_hojas = forms.IntegerField()
    precio = forms.IntegerField()


class buscar(forms.Form):
    """Formulario para ingresar datos en busqueda de sesiones fotograficas"""

    nombre = forms.CharField(max_length=40)
