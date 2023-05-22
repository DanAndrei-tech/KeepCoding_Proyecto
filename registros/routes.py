from registros import app
from datetime import datetime
from flask import render_template, request, redirect, url_for
from registros.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear-coche', methods=['GET', 'POST'])
def crear_coche():
    if request.method == 'POST':
        insert([request.form['marca'],
                request.form['modelo'],
                request.form['precio'],
                request.form['ciudad']])
        return redirect('/')
    
    return render_template('crear_coche.html')

@app.route('/coches')
def mostrar_coches():
   coches = select_all()
   return render_template('coches.html',coches = coches)


@app.route('/coche/<int:coche_id>')
def coche(coche_id):
   coche = select_by(coche_id)
   return render_template('coche.html', coche=coche)

@app.route('/borrar-coche/<int:coche_id>')
def borrar_coche(coche_id):
   coche = select_by(coche_id)
   borrar = delete_by(coche_id)
   return render_template('coches.html', coche=coche)






