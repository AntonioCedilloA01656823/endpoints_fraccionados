from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

# Create your views here.
class Nivel:
    def __init__(self, tema, descripcion):
        self.tema = tema
        self.descripcion = descripcion
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)
    

def index(request):
    return HttpResponse("La pagina indice funciona, Bienvenido a los endpoints")


def login(request):
    return HttpResponse("Login funciona")



@csrf_exempt
def niveles(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    numeroLevel = eljson['num_nivel']

    if (numeroLevel == 1):
        tema = "conjuntos"
        descripcion = "Consigue los elementos que te menciona el juego y llevalos a la olla para conseguir puntos"
        resultado =  Nivel(tema,descripcion)
        res_json = resultado.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    elif (numeroLevel == 2):
        tema = "Operaciones"
        descripcion = "Reune los elementos necesarios que te diga la pantalla en la olla para conseguir puntos"
        resultado =  Nivel(tema,descripcion)
        res_json = resultado.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    elif (numeroLevel == 1):
        tema = "Fracciones"
        descripcion = "Realiza una pizza con las fracciones que te diga la pantalla y consigue puntos"
        resultado =  Nivel(tema,descripcion)
        res_json = resultado.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        tema = "Fracciones"
        descripcion = "Realiza una pizza con las fracciones que te diga la pantalla y consigue puntos"
        resultado = Nivel(tema,descripcion)
        res_json = resultado.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")


def calificacion(response):
    return HttpResponse("Calificacion funciona")
