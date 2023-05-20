from registros import app
from flask import render_template,request,redirect,url_for
from registros.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/Contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/Lenguajes de programacion')
def lenguajes():
    return "<h1>Pagina de lenguajes</h1>"