from flask import Flask, redirect, url_for, render_template
import math
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def date_now():
    return {
        'date': datetime.utcnow()
    }

@app.route('/')
def index():
    # Instrucciones del backend
    return render_template('index.html', edades = [30, 32, 34])

@app.route('/general')
@app.route('/general/<int:a>/<int:b>/<int:c>')
@app.route('/general/<an>/<int:a>/<bn>/<int:b>/<cn>/<int:c>')

def general(a = 1, b = 0, c = 0, an = None, bn = None, cn = None):
    aviso = ""
    xUno = 0
    xDos = 0
    discriminante = (((pow(b, 2))-(4*a*c)))

    if an == 'n':
        a = -a
        b = b
        c = c

    if bn == 'n':
        a = a
        b = -b
        c = c

    if cn == 'n':
        a = a
        b = b
        c = -c

    aviso = ""
    discriminante = math.pow(b, 2) - 4 * a * c
    
    if discriminante > 0:
    # Dos soluciones reales distintas
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        aviso = f"La solución es: x1 = {x1} y x2 = {x2}"
    elif discriminante == 0:
    # Una solución real (raíz doble)
        aviso = ""
        x1 = -b / (2 * a)
        aviso = f"La solución es: x1 = {x1}"
    else:
    # No hay soluciones reales
        aviso = "No hay solución real"

    return render_template('general.html', aviso = aviso, a=a, b=b, c=c)

@app.route('/proyectos')
@app.route('/proyectos/<string:nombre>')
@app.route('/proyectos/<string:nombre>/<int:edad>')
def proyectos(nombre = None, edad = None):
    texto = ""
    if nombre != None and edad != None:
        try:
            int(nombre)
            texto = "solo letras"
                
        except:
            texto = f"Proyecto de {nombre} que tiene {edad} años"
            
    else:
        texto = f"Proyecto sin asignar"
    
    return render_template('proyectos.html', texto = texto)

@app.route('/contacto')
def contacto():
    nombre = "Miguel"
    return render_template('contacto.html')

@app.route('/plantilla')
@app.route('/plantilla/<int:edad>')
def plantilla(edad = 0):
    adultos = [
        "Grey's Anatomy",
        "Game of Thrones",
        "Logan"
    ]
    ninos = [
        "Shrek",
        "Spirit",
        "Hercules"
    ]
    return render_template('plantilla.html', edad = edad, adultos = adultos, ninos = ninos)

if __name__ == '__main__':
    app.run(debug = True)