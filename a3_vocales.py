def contar_vocales(cad):
    vocales = 0
    for c in cad:
        if c in "aeiouAEIOU":
            vocales = vocales + 1
    return vocales

frase =input("ingrese una palabla/frase:    ")
numeroVocales = contar_vocales(frase)
print("la palabra/frase tiene "+str(numeroVocales)+" vocales")
 