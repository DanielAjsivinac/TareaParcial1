import numpy as np
import psycopg2

def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)

def programa():
    ab = ["a:   ", "b:  "]
    print("ingrese 2 numeros enteros (a,b)")
    a = entradaEntera(ab[0])
    b = entradaEntera(ab[1])
    des = []
    if a == b:
        print("a y b iguales")
        return [a,b,a]
    else:
        if a>b:
            mayor = a
            menor = b
        else:
            mayor = b
            menor = a
        
        while mayor >= menor:
            des.append(mayor)
            mayor = mayor - 1
        print(des)
        with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_a6.txt', 'a') as f:
            f.write("Mayor "+str(des[0])+"    Menor: "+ str(des[len(des)-1])+"   Resultado: " + str(des) +"\n")
        return [des[0],des[len(des)-1],des]
    
def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")
#-****************************************
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM Programa_a6')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, mayor,menor, orden):
    curs.execute("INSERT INTO Programa_a6(mayor,menor, orden) VALUES(%s,%s,%s);",(mayor,menor,orden))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Programa_a6')
        conexion.commit()

#------***********************************
while True:
    conexion= conectar()
    cursor= conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        resultado = programa()
        insertar(conexion, cursor,resultado[0],resultado[1],resultado[2])
        input("\n presione para continuar")
    elif opcion == 1:
        obtener(cursor)
        input("\n presione para continuar")
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