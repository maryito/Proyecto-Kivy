#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 
import os.path


def DbPrecio_Sector(coordenada,camino): 
    if coordenada =="S":
        tabla = "area_sur"
        columna = 'AREA'
    elif coordenada =="N":
        tabla = "area_norte"
        columna = 'AREA'
    elif coordenada == "ZONA-SEC":
        tabla= "Zonas_Sectores"
        columna = 'ZONA'
    else:
        tabla= "zonas"
        columna = 'ZONAS'
        
    origen =camino[0]
    destino =camino[1]
    con = None 
    datos=0
    print (origen, tabla ,destino)
    try:
        #traer la dirrecion del archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "Bd_Att.sqlite")
        con = sqlite3.connect(db_path)    
        cur = con.cursor()    
        consulta= ("SELECT {3} FROM '{1}' WHERE {2} LIKE '{0}'".format(origen,tabla,columna,destino.replace(" ","_")))
        cur.execute(consulta)
        datos = cur.fetchone()

    except Exception as e: 
        # si no encuntra la columna intervimos el origen con el destino
        if "no such column" in e.args[0]:
            print ("invertir")
            cur = con.cursor()    
            consulta= ("SELECT {0} FROM '{1}' WHERE {2} LIKE '{3}'".format(origen,tabla,columna,destino.replace(" ","_")))
            cur.execute(consulta)
            datos = cur.fetchone()
        else:
            print("Error %s : "%(e.args[0]) )
    finally:
        if con:
            con.close()
    return datos[0]