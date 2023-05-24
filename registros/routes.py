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
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        if not marca or not modelo or not ciudad:
            flash('Por favor, completa todos los campos')
        elif int(precio) <= 0:
            flash('El precio debe ser mayor que cero')
        else:
            insert([marca, modelo, precio, ciudad])
            flash('Has creado el coche correctamente!')
            return redirect(url_for('mostrar_coches'))

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
   return redirect(url_for('mostrar_coches'))



@app.route('/editar-coche/<int:coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
        update_by(coche_id, {
            'marca': request.form['marca'],
            'modelo': request.form['modelo'],
            'precio': request.form['precio'],
            'ciudad': request.form['ciudad']
        })
        return redirect(url_for('mostrar_coches'))

    coche = select_by(coche_id)
    coches = select_all()
    return render_template('crear_coche.html', coche=coche, coches=coches)






