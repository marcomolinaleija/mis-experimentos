opción="si"
suma=0
while opción == "si":
    v=int(input("ingresa un número"))
    suma = suma + v
    opción=input("quieres cargar otro valor?")
print(f"la suma de los números ingresados es: {suma}")