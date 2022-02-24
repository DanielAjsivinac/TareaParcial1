#vocales = {"a":0, "e": 0, "i": 0, "o":0, "u": 0}
import numpy as np
import psycopg2

def contar_vocales(palabra):
    for c in palabra:
        if c in "aA":
            vocales["a"] = vocales.get("a")+1
        elif c in "eE":
            vocales["e"] = vocales.get("e")+1
        elif c in "iI":
            vocales["i"] = vocales.get("i")+1
        elif c in "oO":
            vocales["o"] = vocales.get("o")+1
        elif c in "uU":
            vocales["u"] = vocales.get("u")+1
    #return vocales

def programa():
    p = input("ingrese una palabra: ")
    contar_vocales(p)
    print(vocales) 
    return p

def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

#**********************************************
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM Programa_a7')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, palabra,a,e,i,o,u):
    curs.execute("INSERT INTO Programa_a7(palabra,_a,_e,_i,_o,_u) VALUES(%s,%s,%s,%s,%s,%s);",(palabra,a,e,i,o,u))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Programa_a7')
        conexion.commit()


#**********************************************
while True:
    vocales = {"a":0, "e": 0, "i": 0, "o":0, "u": 0}
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        palabra = programa()
        insertar(conexion,cursor,palabra,vocales.get("a"),vocales.get("e"),vocales.get("i"),vocales.get("o"),vocales.get("u"))
        input("\n presione para continuar")
    elif opcion == 1:
        obtener(cursor)
        input("\n presione para continuar")
    elif opcion == 2:
        eliminarOpciones(conexion,cursor)
    elif opcion == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()