from pickle import FALSE, TRUE
import numpy as np
import psycopg2
from sympy import true
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    SQL = 'SELECT*FROM Areas;'
    curs.execute(SQL)
    valores= curs.fetchall() 
    print(valores)

def insertar(conexion,curs, Fig, Area):
    curs.execute("INSERT INTO Areas(figura, Area) VALUES(%s,%s);",(Fig, Area))
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
    print("\n0. Triangulo \n1. Circulo \n2. Cuadrado \n3. Rectangulo \n4. Todo ")
    ord = "seleccione opcion a eliminar"
    o = entradaEntera(ord)
    if o ==0:
        curs.execute("DELETE FROM Areas WHERE figura = 'Triangulo'")
        conexion.commit()
    elif o ==1:
        curs.execute("DELETE FROM Areas WHERE tipo = 'Circulo' ")
        conexion.commit()
    elif o==2:
        curs.execute("DELETE FROM Areas WHERE tipo = 'Cuadrado' ")
        conexion.commit()
    elif o==3:
        curs.execute("DELETE FROM Areas WHERE tipo = 'Rectangulo' ")
        conexion.commit()
    elif o==4:
        curs.execute('DELETE FROM Areas')
        conexion.commit()
    else:
        input("ingrese una opcion valida")        
        return eliminarOpciones(conexion, curs)



def Area_triangulo(base, altura):
    area = (base*altura)/2
    return area
def Area_circulo(radio):
    area = np.pi*radio*radio
    return area
def Area_cuadrado_rectangulo(base,altura):
    area = base*altura
    return area
def validarfloat():
        try:
            x = float(input())
            return x
        except:
            print("ingrese un numero")
            return validarfloat()

def menu():
    try:
        print("\n0. Calculo de Areas \n1. Mostrar Historial \n2. Borrar Historial \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

def menuAreas():
    try:
        print("\n0. Triangulo \n1. Circulo \n2. Cuadrado \n3. Rectangulo \n4. Continuar")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        return menuAreas()
fig = {0:'Triangulo', 1: 'Circulo', 2: 'Cuadrado', 3: 'Rectangulo'}

while True:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        buscarArea = True
        while buscarArea == True:
            figura = menuAreas()
            if figura == 0:
                print("ingrese el valor de la base del trangulo")
                base = validarfloat()
                print("ingrese el valor de la altura del triangulo")
                altura = validarfloat()
                area = Area_triangulo(base,altura)                
                buscarArea = False    
            elif figura == 1:
                print("ingrese el radio del circulo")
                radio = validarfloat()
                area = Area_circulo(radio)
                buscarArea = False  
            elif figura == 2:
                print("ingrese el valor del lado")
                lado = validarfloat()
                area = Area_cuadrado_rectangulo(lado,lado)
                buscarArea = False  
            elif figura == 3:
                print("ingrese el valor del lado 1 (base)")
                base = validarfloat()
                print("ingrese el valor del lado 2 (altura)")
                altura = validarfloat()
                area = Area_cuadrado_rectangulo(base, altura)
                buscarArea = False  
            elif figura==4:
                break
            else:
                break
            insertar(conexion,cursor,fig.get(figura),area)
            with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_b4.txt', 'a') as f:
                f.write("Figura: "+str(fig.get(figura))+"    Area : "+ str(area)+"\n")
            print("el area del " + str(fig.get(figura)) + " "+ str(area))
    elif opcion == 1:
        obtener(cursor)
        input("\n presone para continuar")
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
        
