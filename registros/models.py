import sqlite3
from registros import ORIGIN_DATA
from flask import redirect,url_for

def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("select * from coches")
    filas = res.fetchall() #
    columnas= res.description #
                                                          
    #objetivo crear una lista de diccionario con filas y columnas
    lista_diccionario=[]
    
    for f in filas:
        diccionario={}
        posicion=0
        for c in columnas:
            diccionario[c[0]] = f[posicion] 
            posicion +=1
        lista_diccionario.append(diccionario)

    con.close()
    
    return lista_diccionario

def insert():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute(f"insert into coches VALUES(NULL, 'LAMBO','GALLARDO', 100000,'LOSANGELES') ")
    con.commit()

    con.close()

    