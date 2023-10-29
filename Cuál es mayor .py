print("¿Cuál es el número más grande?")
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

if n1 > n2 and n1 > n3:
    print("El número", n1, "es el más grande.")
else:
    if n2 > n3:
        print("El número", n2, "es el más grande.")
    else:
        print("El número", n3, "es el más grande.")
