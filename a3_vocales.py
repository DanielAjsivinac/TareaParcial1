import numpy as np
import psycopg2
def contar_vocales(cad):
    vocales = 0
    for c in cad:
        if c in "aeiouAEIOU":
            vocales = vocales + 1
    return vocales

def programa():
    frase =input("ingrese una palabla/frase (28 caracteres max):    ")
    numeroVocales = contar_vocales(frase)
    print("la palabra/frase tiene "+str(numeroVocales)+" vocales")
    with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_a3.txt', 'a') as f:
                f.write("Palabra: "+str(frase)+"    Numero de Vocales: "+ str(numeroVocales)+"\n")
    return [frase,numeroVocales]

def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")
#---------------conectar------------
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM Programa_a3')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, palabra, vocales):
    curs.execute("INSERT INTO Programa_a3(palabra, numero_vocales) VALUES(%s,%s);",(palabra, vocales))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Programa_a3')
        conexion.commit()


#*******************
while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        resultado = programa()
        insertar(conexion,cursor,resultado[0],resultado[1])
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