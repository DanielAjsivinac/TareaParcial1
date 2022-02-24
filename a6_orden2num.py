def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)
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