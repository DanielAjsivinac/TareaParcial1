from ast import While
from statistics import mode
import sympy
import psycopg2
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")


def insertar(conexion, curs, vector):#ID, Modelo, KmRecorridos, Estado):
    curs.execute("INSERT INTO Taxis(Id_num, ModeloTaxi,KmRecorridos, Condicion_del_taxi) VALUES(%s,%s,%s,%s);",(vector[0],vector[1],vector[2],vector[3]))
    conexion.commit()
    input("Se ha ingresado correctamente")

def enteros(mensaje='colocar mensaje'):
    try:
        print(mensaje)
        x=int(input())
        if x<0:
            return enteros(mensaje)
        else:  return x
    except:
        print("ingrese un numero entero")
        return enteros(mensaje)

def obtener(curs):
    print("\n0. Mostrar Optimo \n1. Mostrar Mantenimiento \n2. Mostrar Mecanico \n3. Mostrar Renovar \n4. Mostrar Todo")

    opci = enteros(mensaje="seleccione una opcion")
    if opci ==0:
        curs.execute("SELECT*FROM Taxis WHERE Condicion_del_taxi = 'Optimo'")
        valores= curs.fetchall() 
    elif opci ==1:
        curs.execute("SELECT*FROM Taxis WHERE Condicion_del_taxi = 'Mantenimiento'")
        valores= curs.fetchall() 
    elif opci ==2:
        curs.execute("SELECT*FROM Taxis WHERE Condicion_del_taxi = 'Mecanico'")
        valores= curs.fetchall() 
    elif opci ==3:
        curs.execute("SELECT*FROM Taxis WHERE Condicion_del_taxi = 'Renovar'")
        valores= curs.fetchall() 
    elif opci == 4:
        curs.execute('SELECT*FROM Taxis')
        valores= curs.fetchall() 
    else:
        input("ingrese una opcion valida")       
    print(valores)
    print("\n")
    input("Presione para continuar")

def eliminar(conexion, curs):
    print("\n0. Por ID \n1. Borrar Todo \n2. Cancelar")
    o = enteros(mensaje="Seleccione una opcion")
    if o ==0:
        eliminarporID(conexion)
    elif o ==1:
        curs.execute('DELETE FROM Taxis')
        conexion.commit()
    elif o==3:
        print(" ")
    else:
        input("ingrese una opcion valida")        
        return eliminar(conexion, curs)


def eliminarporID(conexion):

    id = enteros(mensaje='ingrese el ID del taxi a eliminar')
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Taxis WHERE Id_num = "  + str(id))
    conexion.commit()


def asignar_ID(cursor):
    cursor.execute('SELECT COUNT(*) FROM Taxis')
    a = cursor.fetchall()
    print(a)
    id = a[0]
    print("datos:" +str(id))
    return id 

def insertarDatos(cursor):
    salida = []
    modelo = enteros(mensaje="ingrese el modelo del Taxi (año)")
    KmRec = enteros(mensaje="ingrese el recorrido del taxi en Km")
    if modelo < 2007 and KmRec> 20000:
        condicion = "Renovar"
    elif modelo < 2013 and KmRec==20000:
        condicion = "Mantenimiento"
    elif modelo >2013 and KmRec<10000:
        condicion = "Optimo"
    else:
        condicion = "Mecanico"
    id = asignar_ID(cursor)
    salida = [id, modelo, KmRec, condicion]
    return salida


def menu():
    try:
        print("\n0. Ingresar Taxi \n1. Ver Taxi \n2. Eliminar Taxi \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion==None:
        opcion = menu()
    if opcion==0:
        vector=insertarDatos(cursor)
        insertar(conexion,cursor, vector)
    elif opcion ==1:
        obtener(cursor)
    elif opcion ==2:
        eliminar(conexion, cursor)
    elif opcion == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()