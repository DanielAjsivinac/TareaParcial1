def contar_vocales(cad):
    vocales = 0
    for c in cad:
        if c in "aeiouAEIOU":
            vocales = vocales + 1
    return vocales

def programa():
    frase =input("ingrese una palabla/frase:    ")
    numeroVocales = contar_vocales(frase)
    print("la palabra/frase tiene "+str(numeroVocales)+" vocales")

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