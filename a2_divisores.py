def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def programaDivisores():        #agragar insertar al final (vector de datos)
    print("ingrese un numero: ")
    numero = entradaEntera()
    print("los divisores de " + str(numero)+ " son:")
    for i in range(1, numero+1):
        if(numero % i)==0:
            print(i)

def menu():
    try:
        print("\n0. Correr programa \n1. Ver historial \n2. Eliminar datos \n3. Salir")
        x = int(input())
        return x
    except:
        print("ingrese un numero")
        print("presione para continuar")

while True:
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        programaDivisores()
    elif opcion == 1:
        print("por ahora nada")
    elif opcion == 2:
        print("eliminar")
    elif opcion == 3:
#        cursor.close()
#        conexion.close()
        break
    else:
        print("seleccione una opcion valida")
        input("presione para continuar")
#        cursor.close()
#        conexion.close()