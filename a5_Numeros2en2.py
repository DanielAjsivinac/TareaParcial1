def entradaEntera(orden):
        try:
            print(orden)
            x = int(input())
            return x
        except:
            print("ingrese un numero")
            return entradaEntera(orden)
ord_num = ["numero inicio: ", "numero final: "]
inicio = entradaEntera(ord_num[0])
final = entradaEntera(ord_num[1])
res = []
suma = inicio
for i in range(1,final+1):
    if final>suma:
        res.append(suma) 
        suma = suma+2
print(res)