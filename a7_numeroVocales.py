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

p = input("ingrese una palabra: ")
aeiou = contar_vocales(p)
print(vocales)
