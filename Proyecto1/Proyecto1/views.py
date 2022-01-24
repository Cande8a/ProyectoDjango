from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Template , Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido): 
        self.nombre = nombre
        self.apellido = apellido

#tanto este saludo como la despedida son ejemplos de contenido estático, en cambio el ejemplo de la fecha es ejemplo de contenido dinámico, porque depende del momento en que lo ejecute
def saludo(request): #Función vista (primera vista): devuelve una respuesta con el siguiente texto 

    p1 = Persona("Juanito" , "Perez")

    #nombre = "Juan"
    #apellido = "Perez"
    ahora = datetime.datetime.now()
    temas = ["plantillas", "despliegue", "vistas", "modelo", "formularios"]

    #doc_externo = open("D:/Programacion/ProjectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = loader.get_template('miplantilla.html')
    #ctx = Context({"nombre_persona":p1.nombre , "apellido_persona":p1.apellido , "ahora":ahora , "temas": temas}) 
    #documento = doc_externo.render({"nombre_persona":p1.nombre , "apellido_persona":p1.apellido , "ahora":ahora , "temas": temas})

    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre , "apellido_persona":p1.apellido , "ahora":ahora , "temas": temas})

def despedida(request): 
    documento2 = """<html>
    <body>
    <h1>
    <em>No te olvides mi Pepsi</em>
    </h1>
    </body>
    </html>"""
    return HttpResponse(documento2) 

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento3 = """<html>
    <body>
    <p style= "color:green">
    Fecha y hora actuales %s 
    </p>
    </body>
    </html>""" % fecha_actual #la """ es para que python reconozca esto como todo lo mismo. podria haberlo puesto en la misma linea, pero con simple comilla

    return HttpResponse(documento3)

def calcularEdad(request, edad, anio):
    #edadActual = 30 a esta la habilito, en el caso, por ejemplo, de no pasar edad en el url, entonces dejo aca una edad fija y la saco de los parametros de la funcion
    periodo = anio - 2022
    edadFutura = edad + periodo
    documento4 = "<html><body><h2>En el año %s tendrás %s años" %(anio, edadFutura) #el % antes de los parametros estos es para indicar la posicion de los parametros que pase, en el orden que los pase

    return HttpResponse(documento4)

     