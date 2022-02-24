import sympy

#pedir 3 numeros, 1 mayor->suma, 2do mayor-> multiplicacion, 3ro mayor -> concatenar
def entradaEntera(mensaje):
        try:
            print(mensaje)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(mensaje)

def programanumeros():
    print("ingrese 3 numeros (a,b,c)")
    ord_num = ["a: ", "b: ", "c: "]
    a = entradaEntera(ord_num[0])
    b = entradaEntera(ord_num[1])
    c = entradaEntera(ord_num[2])
    numeros=[a,b,c]
    numeros.sort(reverse=True)
    if a==b:
        if a == c :
            print("todos son iguales")
        else:
            print("numero diferente: " +str(c))
    elif a == c:
        print("numero diferente: " +str(b))
    elif b==c:
        print("numero diferente: " +str(a))
    else:   
        if numeros[0] == a:
            suma = a+b+c
            print(suma)
        elif numeros[0] == b:
            mult = a*b*c
            print(mult)
        elif numeros[0] == c:
            print(str(a)+str(b)+str(c))
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

while True:
    opcion = menu()
    while opcion == None:
        opcion = menu()
    if opcion == 0:
        programanumeros()
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