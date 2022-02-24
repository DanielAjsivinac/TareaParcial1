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
    SQL = 'SELECT*FROM Triangulos;'
    curs.execute(SQL)
    valores= curs.fetchall() 
    print(valores)

def insertar(conexion,curs, tipo, ladoA, ladoB, ladoC):
    curs.execute("INSERT INTO Triangulos(tipo, lado_a, lado_b, lado_c) VALUES(%s,%s,%s,%s);",(tipo, ladoA, ladoB, ladoC))
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

def menu():
    try:
        print("\n0. Clasifica triangulos \n1. Mostrar Historial \n2. Borrar Historial \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)
            
while True:
    conexion = conectar()
    cursor = conexion.cursor()
    x = menu()
    while x == None:
        x=menu()
    if x == 0:
        print("ingrese el valor(entero) de los 3 lados del trangulo (a,b,c)")
        lado = ["lado a: ", "lado b: ", "lado c: "]
        A = entradaEntera(lado[0])
        B = entradaEntera(lado[1])
        C = entradaEntera(lado[2])
        if A<(B+C) and B<(A+C) and C<(A+B):
            if A ==B  and A==C:
                triangulo = "Equilatero"
                print(triangulo)
            elif A==B or A==C or C==B:
                triangulo = "Isoceles"
                print(triangulo)
            else:
                triangulo = "Escaleno"
                print(triangulo)
            insertar(conexion, cursor, triangulo, A, B, C)
            with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_b2.txt', 'a') as f:
                f.write("Triangulo: "+str(triangulo)+"    Lados(a,b,c) : "+ str(A)+", "+ str(B)+", "+str(C)+"\n")
        else:
            print("ingrese valores que cumplan con a<(b+c) & b<(a+c) & c<(a+b) para formar un triangulo")
    elif x == 1:
        obtener(cursor)
        input("\n presone para continuar")
    elif x == 2:
        print("---Eliminar---")
        eliminarOpciones(conexion, cursor)
    elif x == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()