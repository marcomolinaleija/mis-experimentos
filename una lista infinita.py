números=[]
valor=int(input("ingresa un número"))
while valor != 0:
    números.append(valor)
    valor=int(input("ingresa un número(0 para terminar el programa)"))
print(f"los elementos de la lista son: {len(números)}")