nota1=int(input("ingresa primer nota"))
nota2=int(input("ingresa segunda nota"))
nota3=int(input("ingresa tercera nota"))
promedio=(nota1+nota2+nota3)/3
if promedio>=7:
    print(f"has aprobado con una calificación de {promedio}.")
else:
    if promedio>=5:
        print(f"regular. tu promedio es de {promedio}.")
    else:
        print(f"tu promedio es de {promedio}. has reprobado, wey")