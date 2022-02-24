from sympy import true
import numpy as np
import psycopg2
#---------------Postgres----------------
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    print("\n0. Mostrar Aprobados \n1. Mostrar Reprobados \n2. Mostrar Todo")
    ord = "seleccione una opcion"
    opci = entradaEntera(ord)
    if opci ==0:
        curs.execute("SELECT*FROM Notas WHERE estado = 'Aprobado'")
        valores= curs.fetchall() 
    elif opci ==1:
        curs.execute("SELECT*FROM Notas WHERE estado = 'Reprobado'")
        valores= curs.fetchall() 
    elif opci ==2:
        curs.execute('SELECT*FROM Notas')
        valores= curs.fetchall() 
    else:
        input("ingrese una opcion valida")       
    print(valores)

def insertar(conexion,curs, Estado, Promedio):
    curs.execute("INSERT INTO Notas(Estado, promedio) VALUES(%s,%s);",(Estado, Promedio))
    conexion.commit()


def eliminarOpciones(conexion, curs):
    print("\n0. Borrar Aprobados \n1. Borrar Reprobados \n2. Borrar Todo \n3. Cancelar")
    ord = "seleccione una opcion"
    o = entradaEntera(ord)
    if o ==0:
        curs.execute("DELETE FROM Notas WHERE estado = 'Aprobado'")
        conexion.commit()
    elif o ==1:
        curs.execute("DELETE FROM Notas WHERE tipo = 'Reprobado' ")
        conexion.commit()
    elif o==2:
        curs.execute('DELETE FROM Notas')
        conexion.commit()
    elif o==3:
        print(" ")
    else:
        input("ingrese una opcion valida")        
        return eliminarOpciones(conexion, curs)
#------------------enteros--------------
def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)

#-------------programaNotas-------------
def aprobar_reprobar(a,b,c):
    promedio = (a+b+c)/3
    if promedio<60:
        resultado = [promedio, "Reprobado"]
        return resultado
    else :
        resultado = [promedio, "Aprobado"]
        return resultado

def entradaNotas(calificacion):
        try:
            print("ingrese un entero entre 0 y 100")
            print(calificacion)
            x = int(input())
            if x<0:
                return entradaEntera(calificacion)
            elif x>100:
                return entradaEntera(calificacion)
            else:
                return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def menu():
    try:
        print("\n0. Ingreso de notas \n1. Mostrar Historial \n2. Borrar Historial \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")


while true:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion==None:
        opcion = menu()
    if opcion == 0:
        notas = ["nota 1","nota 2","nota 3"]
        a = entradaNotas(notas[0])
        b = entradaNotas(notas[1])
        c = entradaNotas(notas[2])
        Resultado = aprobar_reprobar(a,b,c)
        print("promedio: " + str(Resultado[0])+ "Estado: " + Resultado[1])

        insertar(conexion,cursor,Resultado[1],Resultado[0])
    elif opcion == 1:
        obtener(cursor)
        input("presione para continuar")
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
        