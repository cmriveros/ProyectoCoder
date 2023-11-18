from django.http import HttpResponse
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