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
    ord_num = ["numero inicio: ", "numero final: "]
    inicio = entradaEntera(ord_num[0])
    final = entradaEntera(ord_num[1])
    res = []
    suma = inicio
    if inicio > final:
        resta = inicio 
        for i in range(1+inicio+1):
            if final<=resta:
                res.append(resta)
                resta= resta-2
    else:
        for i in range(1,final+1):
            if final>=suma:
                res.append(suma) 
                suma = suma+2
    print(res)
    with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_a5.txt', 'a') as f:
            f.write("Inicio: "+str(inicio)+"    Final: "+ str(final)+"  Orden: "+str(res)+"\n")
    return [inicio,final,res]

def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")
#**************DATOS*********************
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM Programa_a5')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, numero_i,numero_f, vector):
    curs.execute("INSERT INTO Programa_a5(numero_i,numero_f, numeros2_2) VALUES(%s,%s,%s);",(numero_i,numero_f,vector))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Programa_a5')
        conexion.commit()

#****************************************
while True:
    conexion = conectar()
    cursor = conexion.cursor() 
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        resultado =programa()
        #print(resultado)
        insertar(conexion,cursor,resultado[0], resultado[1],resultado[2])
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