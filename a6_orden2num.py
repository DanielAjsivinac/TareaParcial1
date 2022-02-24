def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)

def programa():
    ab = ["a:   ", "b:  "]
    print("ingrese 2 numeros enteros (a,b)")
    a = entradaEntera(ab[0])
    b = entradaEntera(ab[1])
    des = []
    if a>b:
        mayor = a
        menor = b
    elif a<b:
        mayor = b
        menor = a
    else :
        print("a y b iguales")
    while mayor >= menor:
        des.append(mayor)
        mayor = mayor - 1
    print(des)
    
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