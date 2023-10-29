print("vamos a verificar si un número es par o impar.")

número = int(input("ingresa un número entero"))
if número % 2 == 0:
    print("el número, ", número, " es par") 
elif número % 2 == 1:
    print("el número", número, " es impar")