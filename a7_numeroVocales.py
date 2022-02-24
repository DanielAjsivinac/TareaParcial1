vocales = {"a":0, "e": 0, "i": 0, "o":0, "u": 0}
def contar_vocales(palabra):
    for c in palabra:
        if c in "aA":
            vocales["a"] = vocales.get("a")+1
        elif c in "eE":
            vocales["e"] = vocales.get("e")+1
        elif c in "iI":
            vocales["i"] = vocales.get("i")+1
        elif c in "oO":
            vocales["o"] = vocales.get("o")+1
        elif c in "uU":
            vocales["u"] = vocales.get("u")+1
    return vocales

def programa():
    p = input("ingrese una palabra: ")
    aeiou = contar_vocales(p)
    print(aeiou)

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