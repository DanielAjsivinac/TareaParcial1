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
    SQL = 'SELECT*FROM Prueba_vectores;'
    curs.execute(SQL)
    valores= curs.fetchall() 
    print(valores)

def insertar(conexion,curs, vector, numero):
    curs.execute("INSERT INTO Prueba_vectores(vector,total_impares) VALUES(%s,%s);",(vector, numero))
    conexion.commit()

def eliminarhistorial(conexion, curs):
     curs.execute('DELETE FROM Prueba_vectores')
     conexion.commit()

def menu():
    try:
        print("\n0. Programa Impares \n1. Mostrar Historial \n2. Borrar Historial \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

while TRUE:
    conexion = conectar()
    cursor = conexion.cursor()
    w = menu()
    while w==None:
        w = menu()
    if w == 0:
        numImpar = []
        for i in range(1,101):
            if i % 2 != 0:
                numImpar.append(i)
        print("impares: " + str(numImpar))
        print("numero impares: "+ str(len(numImpar)))
        insertar(conexion,cursor,numImpar,len(numImpar))
        with open('C:\\Users\\Usuario FAX\\Documents\\DANI\\TAREAS\\proyectos AIE\\tarea1P\\TareaParcial1\\Salida_b1.txt', 'a') as f:
            f.write("Impares: "+str(numImpar)+"    Cantidad: "+ str(len(numImpar))+"\n")
        input("presione para continuar")
    elif w == 1:
        obtener(cursor)
        input("\n presone para continuar")
    elif w == 2:
        eliminarhistorial(conexion, cursor)
    elif w == 3:
        cursor.close()
        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
        cursor.close()
        conexion.close()
        