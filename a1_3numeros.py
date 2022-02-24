from asyncio.windows_events import NULL
import sympy
import psycopg2
#pedir 3 numeros, 1 mayor->suma, 2do mayor-> multiplicacion, 3ro mayor -> concatenar
def entradaEntera(mensaje):
        try:
            print(mensaje)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(mensaje)

def programanumeros(conexion,cursor):
    print("ingrese 3 numeros (a,b,c)")
    ord_num = ["a: ", "b: ", "c: "]
    a = entradaEntera(ord_num[0])
    b = entradaEntera(ord_num[1])
    c = entradaEntera(ord_num[2])
    print("\n")
    numeros=[a,b,c]
    OrdenIngreso = [a,b,c]
    numeros.sort(reverse=True)
    if a==b:
        if a == c :
            print("todos son iguales")
            insertar(conexion,cursor,"Todos iguales",OrdenIngreso, NULL)
        else:
            print("numero diferente: " +str(c))
            insertar(conexion,cursor,"dos iguales", OrdenIngreso, NULL)
    elif a == c:
        print("numero diferente: " +str(b))
        insertar(conexion,cursor,"dos iguales", OrdenIngreso, NULL)
    elif b==c:
        print("numero diferente: " +str(a))
        insertar(conexion,cursor,"dos iguales", OrdenIngreso, NULL)
    else:   
        if numeros[0] == a:
            suma = a+b+c
            print(suma)
            insertar(conexion,cursor,"Suma",OrdenIngreso, suma)
        elif numeros[0] == b:
            mult = a*b*c
            print(mult)
            insertar(conexion,cursor,"Multiplicacion",OrdenIngreso, mult)
        elif numeros[0] == c:
            con =str(a)+str(b)+str(c)
            print(con)
            insertar(conexion,cursor,"Concatenar",OrdenIngreso, con)
        else:
            print("ocurrio un error")
        
def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

#almacenar datos (conectar,llenado de tablas, eliminar datos)

def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    print("\n0. Mostrar Suma \n1. Mostrar Multiplicacion \n2. Mostrar Concatenar \n3. Mostrar Todo")
    ord = "seleccione una opcion"
    opci = entradaEntera(ord)
    if opci ==0:
        curs.execute("SELECT*FROM Programa_a1 WHERE accion = 'Suma'")
        valores= curs.fetchall() 
    elif opci ==1:
        curs.execute("SELECT*FROM Programa_a1 WHERE accion = 'Multiplicacion'")
        valores= curs.fetchall() 
    elif opci ==2:
        curs.execute("SELECT*FROM Programa_a1 WHERE accion = 'Concatenar'")
        valores= curs.fetchall() 
    elif opci == 3:
        curs.execute('SELECT*FROM Programa_a1')
        valores= curs.fetchall() 
    else:
        input("ingrese una opcion valida")       
    print(valores)

def insertar(conexion,curs, accion, vector, resultado):
    curs.execute("INSERT INTO Programa_a1(accion, numeros, resultado) VALUES(%s,%s,%s);",(accion, vector, resultado))
    conexion.commit()

def eliminarOpciones(conexion, curs):
    print("\n0. Suma \n1. Multiplicacion \n2. Concatenar \n3. Todo ")
    ord = "seleccione opcion a eliminar"
    o = entradaEntera(ord)
    if o ==0:
        curs.execute("DELETE FROM Programa_a1 WHERE accion = 'Suma'")
        conexion.commit()
    elif o ==1:
        curs.execute("DELETE FROM Programa_a1 WHERE accion = 'Multiplicacion' ")
        conexion.commit()
    elif o==2:
        curs.execute("DELETE FROM Programa_a1 WHERE accion = 'Concatenar' ")
        conexion.commit()

    elif o==3:
        curs.execute('DELETE FROM Programa_a1')
        conexion.commit()
    else:
        input("ingrese una opcion valida")        
        return eliminarOpciones(conexion, curs)

#------------------------

while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        programanumeros(conexion, cursor)
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
