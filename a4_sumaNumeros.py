def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()
print("ingrese un numero")
numero = entradaEntera()
suma = 0
for i in range(0,numero+1):
    suma = suma +i
 #   print("i: " +str(i))
 #   print ("suma: " +str(suma))

print("la suma: " +str(suma))