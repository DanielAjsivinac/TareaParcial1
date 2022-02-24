from pickle import TRUE
import psycopg2
def conectar():
    try:
        conexion = psycopg2.connect(
            host = "localhost",port = "5432", database = "TareaP1", user = "postgres", password = "123456")
        return conexion
    except psycopg2.Error: 
        print("no se pudo conectar")

def obtener(curs):
    SQL = 'SELECT*FROM Factorial;'
    curs.execute(SQL)
    valores= curs.fetchall() 
    print(valores)

def insertar(conexion,curs, numero, factorial):
    curs.execute("INSERT INTO Factorial(numero,factorial) VALUES(%s,%s);",(numero, factorial))
    conexion.commit()

def eliminarOpciones(conexion, curs):
    print("\n0. Equilatero \n1. Isoceles \n2. Escaleno \n3. Todo ")
    ord = "seleccione opcion a eliminar"
    o = entradaEntera(ord)
    if o ==0:
        curs.execute("DELETE FROM Triangulos WHERE tipo = 'Equilatero'")
        conexion.commit()
    elif o ==1:
        curs.execute("DELETE FROM Triangulos WHERE tipo = 'Isoceles' ")
        conexion.commit()
    elif o==2:
        curs.execute("DELETE FROM Triangulos WHERE tipo = 'Escaleno' ")
        conexion.commit()

    elif o==3:
        curs.execute('DELETE FROM Triangulos')
        conexion.commit()
    else:
        input("ingrese una opcion valida")        
        return eliminarOpciones(conexion, curs)

def eliminarhistorial(conexion, curs):
     curs.execute('DELETE FROM Factorial')
     conexion.commit()

def menu():
    try:
        print("\n0. Programa Factorial \n1. Mostrar Historial \n2. Borrar Historial \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

def factorial(num):             # factorial de numeros diferentes de 0
    fact=1
    for i in range (1,num+1):
        fact = fact*i
    return fact

def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            if x<0 :
                print("ingrese un numero positivo")
                return entradaEntera(orden)
            else:
                return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)

while TRUE:
    conexion = conectar()
    cursor = conexion.cursor()
    opcion = menu()
    while opcion==None:
        opcion = menu()
    if opcion == 0:
        a = "ingrese un numero entero divisible entre 7"
        numero = entradaEntera(a)
        if numero % 7 == 0:
            fact = factorial(numero)
            print(fact)
            insertar(conexion,cursor,numero,fact)
            with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_b3.txt', 'a') as f:
                f.write("Numero: "+str(numero)+"    Factorial: "+ str(fact)+"\n")
        else:
            print("el numero ingresado no es divisible entre 7")
    elif opcion == 1:
        obtener(cursor)
        input("\n presone para continuar")
    elif opcion==2:
        eliminarhistorial(conexion,cursor)
    elif opcion ==3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()