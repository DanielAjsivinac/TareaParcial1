def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()

def programa():
    print("ingrese un numero")
    numero = entradaEntera()
    suma = 0
    for i in range(0,numero+1):
        suma = suma +i
    #   print("i: " +str(i))
    #   print ("suma: " +str(suma))

    print("la suma: " +str(suma))

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
        programa()
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