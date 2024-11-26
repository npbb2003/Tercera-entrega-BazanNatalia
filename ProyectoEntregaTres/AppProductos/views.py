from django.shortcuts import render
from django.http import HttpResponse
from AppProductos.models import SesionFotografica, Fotolibro, CopiaImpresa
from AppProductos.forms import SesionFormulario, CopiaFormulario, FotolibroFormulario


# Create your views here.
def inicio(req):

    return render(req, "appproductos/index.html")


def sesionesFotograficas(req):

    return render(req, "appproductos/sesionesFotograficas.html")


def copiasImpresas(req):

    return render(req, "appproductos/copias.html")


def fotolibros(req):

    return render(req, "appproductos/fotolibros.html")


# def sesionesFormulario(req):
#     if req.method == "POST":
#         sesion = SesionFotografica(
#             nombre=req.POST["nombre"],
#             descripcion=req.POST["descripcion"],
#             precio=req.POST["precio"],
#             activo=True,
#         )

#         sesion.save()

#         return render(req, "AppProductos/index.html")

#     return render(req, "AppProductos/sesionesFormulario.html")


def sesionesFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = SesionFormulario(
            request.POST
        )  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = (
                miFormulario.cleaned_data
            )  # Obtenemos los datos limpios y validados
            sesion = SesionFotografica(
                nombre=informacion["nombre"],
                descripcion=informacion["descripcion"],
                precio=informacion["precio"],
            )  # Creamos un objeto Curso
            sesion.save()  # Guardamos el curso en la base de datos
            return render(
                request, "AppProductos/index.html"
            )  # Redirigimos a la página de inicio
    else:
        miFormulario = (
            SesionFormulario()
        )  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(
        request, "AppProductos/sesionesFormulario.html", {"miFormulario": miFormulario}
    )


def copiasFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = CopiaFormulario(
            request.POST
        )  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = (
                miFormulario.cleaned_data
            )  # Obtenemos los datos limpios y validados
            copia = CopiaImpresa(
                superficie=informacion["superficie"],
                tamanio=informacion["tamanio"],
                precio=informacion["precio"],
            )  # Creamos un objeto Curso
            copia.save()  # Guardamos el curso en la base de datos
            return render(
                request, "AppProductos/index.html"
            )  # Redirigimos a la página de inicio
    else:
        miFormulario = (
            CopiaFormulario()
        )  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(
        request, "AppProductos/copiasFormulario.html", {"miFormulario": miFormulario}
    )


def fotolibrosFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = FotolibroFormulario(
            request.POST
        )  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = (
                miFormulario.cleaned_data
            )  # Obtenemos los datos limpios y validados
            fotolibro = Fotolibro(
                tamanio=informacion["tamanio"],
                cant_hojas=informacion["cant_hojas"],
                precio=informacion["precio"],
            )  # Creamos un objeto Curso
            fotolibro.save()  # Guardamos el curso en la base de datos
            return render(
                request, "AppProductos/index.html"
            )  # Redirigimos a la página de inicio
    else:
        miFormulario = (
            FotolibroFormulario()
        )  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(
        request,
        "AppProductos/fotolibrosFormulario.html",
        {"miFormulario": miFormulario},
    )


def busquedaSesiones(req):
    return render(req, "AppProductos/busquedaSesiones.html")


def buscar(req):
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        lista = SesionFotografica.objects.filter(nombre__icontains=nombre)

        return render(
            req,
            "AppProductos/resultadosBusquedaSesiones.html",
            {"sesiones": lista, "nombre": nombre},
        )

    else:
        respuesta = "Sin datos"
        return HttpResponse(respuesta)
