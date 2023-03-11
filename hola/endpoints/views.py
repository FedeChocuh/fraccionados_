from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import random

# Create your views here.

class Scoreboard:
    def __init__(self,intento1,intento2,intento3,intento4,intento5):
        self.intento1 = intento1
        self.intento2 = intento2
        self.intento3 = intento3
        self.intento4 = intento4
        self.intento5 = intento5 

class Tiempo:
     def __init__(self, minutos,segundos):
        self.minutos = minutos
        self.segundos = segundos
     def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

class Nivel:
    def __init__(self, tema, descripcion):
        self.tema = tema
        self.descripcion = descripcion
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

class Verificacion:
    def __init__(self, valido, saludo):
        self.valido = valido
        self.saludo = saludo
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

class Calificacion:
    def __init__(self, numero):
        self.numero = numero
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)
    

class Stats:
    def __init__(self, tiempo_promedio,tasa_exito,problemas_resueltos):
        self.tiempo_promedio = tiempo_promedio
        self.tasa_exito = tasa_exito
        self.problemas_resueltos = problemas_resueltos
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)


class Save:
    def __init__(self, fraccion_actual,preguntas_respondidas,preguntas_correctas,tiempo_jugado):
        self.fraccion_actual = fraccion_actual
        self.preguntas_respondidas = preguntas_respondidas
        self.preguntas_correctas = preguntas_correctas
        self.tiempo_jugado = tiempo_jugado
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)   



def index(request):
    return HttpResponse("La pagina indice funciona, Bienvenido a los endpoints")

@csrf_exempt
def login(request):
    print("Se realiza el login")
    body = request.body.decode('UTF-8')
    jsoncito = loads(body)
    numLista = jsoncito['num_lista']
    grupo = jsoncito['grupo']
    grado = jsoncito['grado']

    if (numLista in range(1,28)) and (grupo == "A") or (grupo == "B") and (grado in range(1,6)):
        validation = True
        greet = "Bienvenid@"
        res = Verificacion(validation,greet)
        res_json = res.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        validation = False
        greet = "Intenta de nuevo."
        res = Verificacion(validation,greet)
        res_json = res.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")



@csrf_exempt
def niveles(request):
    print("Se realiza el output de niveles")
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

@csrf_exempt
def calificacion(request):
    print("Realizando calificacion")
    body = request.body.decode('UTF-8')
    jsoncito = loads(body)
    numLista = jsoncito['num_lista']
    grupo = jsoncito['grupo']
    grado = jsoncito['grado']

    if (numLista in range(1,28)) and (grupo == "A") or (grupo == "B") and (grado in range(1,6)):
        calif = random.randint(1,10)
        res = Calificacion(calif)
        res_json = res.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        calif = None
        res = Calificacion(calif)
        res_json = res.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    

@csrf_exempt
def tiempo(request):
    print("Realizando tiempo")
    body = request.body.decode('UTF-8')
    jsoncito = loads(body)

    numLista = jsoncito['num_lista']
    grupo = jsoncito['grupo']
    grado = jsoncito['grado']

    if (numLista in range(1,28)) and (grupo == "A") or (grupo == "B") and (grado in range(1,6)):
        m = random.randint(0,59)
        s = random.randint(0,59)
        res = Tiempo(m,s)
        res_json = res.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        m = None
        s = None
        res = Tiempo(m,s)
        res_json = res.toJSON()
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")

@csrf_exempt
def stats(request):
    print('Realizando stats')
    body = request.body.decode('UTF-8')
    jsoncito = loads(body)
    jsoncito = loads(body)
    numLista = jsoncito['num_lista']
    grupo = jsoncito['grupo']
    grado = jsoncito['grado']

    if (numLista in range(1,28)) and (grupo == "A") or (grupo == "B") and (grado in range(1,6)):
        tiempo = str(random.randint(1,1000)) + "segundos"
        tasa = random.randint(1,100)
        problemas = random.randint(1,15)
        res = Stats(tiempo,tasa,problemas)
        res_json = res.toJSON(res)
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        tiempo = None
        tasa = None
        res =  None
        res = Stats(tiempo,tasa,problemas)
        res_json = res.toJSON(res)
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
@csrf_exempt
def save(request):
    print("Realizando save")
    body = request.body.decode('UTF-8')
    jsoncito = loads(body)
    jsoncito = loads(body)
    numLista = jsoncito['num_lista']
    grupo = jsoncito['grupo']
    grado = jsoncito['grado']

    if (numLista in range(1,28)) and (grupo == "A") or (grupo == "B") and (grado in range(1,6)):
        fraccion = str(random.randint(1,8))+"/"+str(random.randint(2,4))
        pregRes = random.randint(0,10)
        pregCor = random.randint(0,10)
        tiempo = random.randint(0,5000)
        res = Save(fraccion,pregCor,pregRes,tiempo)
        res_json = res.toJSON(res)
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        fraccion = None
        pregRes = None
        pregCor = None
        tiempo = None
        res = Save(fraccion,pregCor,pregRes,tiempo)
        res_json = res.toJSON(res)
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")

def scoreboard(request):
    print("Realizando scoreboard")
    body = request.body.decode('UTF-8')
    jsoncito = loads(body)
    jsoncito = loads(body)
    numLista = jsoncito['num_lista']
    grupo = jsoncito['grupo']
    grado = jsoncito['grado']

    if (numLista in range(1,28)) and (grupo == "A") or (grupo == "B") and (grado in range(1,6)):
        i1 = random.randint(0,50)
        i2 = random.randint(0,50)
        i3 = random.randint(0,50)
        i4 = random.randint(0,50)
        i5 = random.randint(0,50)
        res =  Scoreboard(i1,i2,i3,i4,i5)
        res_json = res.toJSON(res)
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")
    
    else:
        i1 = None
        i2 = None
        i3 = None
        i4 = None
        i5 = None
        res =  Scoreboard(i1,i2,i3,i4,i5)
        res_json = res.toJSON(res)
        return HttpResponse(res_json,content_type ="text/json-comment-filtered")

