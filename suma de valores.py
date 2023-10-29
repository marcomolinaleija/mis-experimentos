opción="si"
suma=0
while opción =="si":
    valor=int(input("ingrece un valor"))
    suma = suma + valor
    opción=input("quieres agregar otro valor?")
    print(f"la suma de valores ingrezados es: {suma}")