from ast import While
import sympy
import numpy as np
import psycopg2

def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    print("\n0. Mostrar años bisiestos \n1. Mostrar años no bisiestos \n2. Mostrar Todo")
    ord = "seleccione una opcion"
    opci = entradaEntera(ord)
    if opci ==0:
        curs.execute("SELECT*FROM Bisiesto WHERE bisiesto_no = 'bisiesto'")
        valores= curs.fetchall() 
    elif opci ==1:
        curs.execute("SELECT*FROM Bisiesto WHERE bisiesto_no = 'no bisiesto'")
        valores= curs.fetchall() 
    elif opci ==2:
        curs.execute('SELECT*FROM Bisiesto')
        valores= curs.fetchall() 
    else:
        input("ingrese una opcion valida")       
    print(valores)

def insertar(conexion,curs, Estado, Año):
    curs.execute("INSERT INTO Bisiesto(bisiesto_no, a_ño) VALUES(%s,%s);",(Estado, Año))
    conexion.commit()

def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)

def eliminarOpciones(conexion, curs):
    print("\n0. Borrar Bisiestos \n1. Borrar No Bisiestos \n2. Borrar Todo \n3. Cancelar")
    ord = "seleccione una opcion"
    o = entradaEntera(ord)
    if o ==0:
        curs.execute("DELETE FROM Bisiesto WHERE bisiesto_no = 'bisiesto'")
        conexion.commit()
    elif o ==1:
        curs.execute("DELETE FROM Bisiesto WHERE bisiesto_no = 'no bisiesto' ")
        conexion.commit()
    elif o==2:
        curs.execute('DELETE FROM Bisiesto')
        conexion.commit()
    elif o==3:
        print(" ")
    else:
        input("ingrese una opcion valida")        
        return eliminarOpciones(conexion, curs)

def Año_bisiesto(año):
    if año%100==0:
        clasificacion=[año,"no bisiesto"]
        if año%400==0:
            clasificacion=[año,"bisiesto"]
        return clasificacion
    else:
        if año%4==0:
            clasificacion=[año,"bisiesto"]
            return clasificacion
        else:
            clasificacion=[año,"no bisiesto"]
            return clasificacion

def enterosPositivos(mensaje):
        try:
            print(mensaje)
            x = int(input())
            if x < 0:
                return enterosPositivos(mensaje)
            else:
                return x
        except:
            print("ingrese un numero")
            return enterosPositivos(mensaje)

def menu():
    try:
        print("\n0. Buscar año bisiesto \n1. Ver Historial \n2. Eliminar Historial \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")


while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:        
        mensaje="ingrese su año de nacimiento"
        año = enterosPositivos(mensaje)
        bisiesto = Año_bisiesto(año)
        print(bisiesto)
        insertar(conexion,cursor,bisiesto[1],bisiesto[0])
    elif opcion == 1:
        obtener(cursor)
    elif opcion == 2:
        eliminarOpciones(conexion, cursor)
    elif opcion == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()