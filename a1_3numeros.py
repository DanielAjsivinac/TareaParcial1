#pedir 3 numeros, 1 mayor->suma, 2do mayor-> multiplicacion, 3ro mayor -> concatenar
def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)

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