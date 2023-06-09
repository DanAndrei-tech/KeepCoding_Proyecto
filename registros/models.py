import sqlite3
from registros import ORIGIN_DATA
from flask import redirect,url_for,flash,render_template

def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM coches ORDER BY id DESC")
    coches = res.fetchall() 
    cur.close()

    return coches

                                                          
def insert(registroForm):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute(f"insert into coches(marca, modelo, precio, ciudad) values (?, ?, ?, ?)", registroForm)
    con.commit()
    con.close()



def select_by(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute(f"select * from coches where id={id}")
    
    resultado = res.fetchall()
    con.close()

    if resultado:
        return resultado[0]
    else:
        return None



def delete_by(coche_id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    cur.execute(f"delete from coches where id={coche_id}")

    con.commit()

    flash('El coche ha sido eliminado')
    con.close()
    return redirect(url_for('coche', coche_id=coche_id))

def update_by(coche_id, registro):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()

    cur.execute('''
        UPDATE coches
        SET marca = ?,
            modelo = ?,
            precio = ?,
            ciudad = ?
        WHERE id = ?
    ''', (registro['marca'], registro['modelo'], registro['precio'], registro['ciudad'], coche_id))

    con.commit()
    flash('Has editado el coche correctamente')
    con.close()
