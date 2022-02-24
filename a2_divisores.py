import numpy as np
import psycopg2
#----------------------------------
def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def programaDivisores():        
    print("ingrese un numero: ")
    numero = entradaEntera()
    divisores = []
    print("los divisores de " + str(numero)+ " son:")
    for i in range(1, numero+1):
        if(numero % i)==0:
            #print(i)
            divisores.append(i)
    print(divisores)
    with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_a2.txt', 'a') as f:
                f.write("Numero: "+str(numero)+"    Divisores: "+ str(divisores)+"\n")
    return [numero, divisores]

def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

#conexion, editar tabla

def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    curs.execute('SELECT*FROM Programa_a2')
    valores= curs.fetchall()
    print(valores)

def insertar(conexion,curs, numero, divisores):
    curs.execute("INSERT INTO Programa_a2(numero, divisores) VALUES(%s,%s);",(numero, divisores))
    conexion.commit()

def eliminarOpciones(conexion, curs):
        curs.execute('DELETE FROM Programa_a2')
        conexion.commit()


#*******************************************
while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        resultado = programaDivisores()
        insertar(conexion,cursor,resultado[0],resultado[1])
        input("\n Presione para continuar")
#        print (resultado[0])
#        print(resultado[1])
    elif opcion == 1:
        obtener(cursor)
        input("\n Presione para continuar")
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