from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoTexto = f"Hoy es el dia: {dia}"
    return HttpResponse(documentoTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"mi nombre es <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def probando_template(request):

    nombre = "Carlos"
    apellido = "Riveros"
    lista_de_notas = [1,2,3,4,5,6,7]

    # FORMA SIN EL LOADER
    # diccionario = {"nombre": nombre, "apellido": apellido, "hoy": datetime.datetime.now(), "notas": lista_de_notas} # para enviar contexto
    # mi_html = open("/Users/hp/Desktop/estudio/CODERHOUSE/Python/ProyectoCoder/ProyectoCoder/templates/template1.html", "r")
    # plantilla = Template(mi_html.read())
    # mi_html.close()
    # mi_contexto = Context(diccionario)
    # documento = plantilla.render(mi_contexto)

    diccionario = {"nombre": nombre, "apellido": apellido, "hoy": datetime.datetime.now(), "notas": lista_de_notas} # para enviar contexto
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)