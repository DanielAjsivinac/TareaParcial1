def entradaEntera():
        try:
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera()
print("ingrese un numero: ")
numero = entradaEntera()
print("los divisores de " + str(numero)+ " son:")
for i in range(1, numero+1):
    if(numero % i)==0:
        print(i)