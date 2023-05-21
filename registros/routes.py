from registros import app
from datetime import datetime
from flask import render_template,request,redirect,url_for
from registros.models import *

@app.route('/')
def index():
    return render_template('index.html',
                           dato1 = 'Valor',
                           dato2 = 'Valor2')

@app.route('/insertar-coche')
def insertar_coche():
    insert()
    return redirect('/')

   

@app.route('/Contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/Lenguajes de programacion')
def lenguajes():
    return "<h1>Pagina de lenguajes</h1>"