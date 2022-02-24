import numpy as np
import psycopg2

def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def programa():
    print("ingrese un numero")
    numero = entradaEntera()
    suma = 0
    for i in range(0,numero+1):
        suma = suma +i
    print("la suma: " +str(suma))
    return [numero,suma]

def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")
#***************************
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM Programa_a4')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, numero, suma):
    curs.execute("INSERT INTO Programa_a4(numero, suma) VALUES(%s,%s);",(numero, suma))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Programa_a4')
        conexion.commit()


#***************************
while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        resultado =programa()
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