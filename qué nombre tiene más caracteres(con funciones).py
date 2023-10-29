def caracteres(string):
    return len(string)

nombre1=input("ingresa el primer nombre")
nombre2=input("ingresa el segundo nombre")
nick1=caracteres(nombre1)
nick2=caracteres(nombre2)
if nick1 == nick2:
    print(f"los nombres {nombre1} y {nombre2} tienen la misma cantidad de caracteres. la cantidad de caracteres es de: {nick1},  y {nick2}")
else:
    if nick1 > nick2:
        print(f"el nombre de {nombre1} tiene más caracteres. la cantidad es de: {nick1}")
    else:
        print(f"el nombre de {nombre2} tiene más caracteres. la cantidad es de: {nick2}")