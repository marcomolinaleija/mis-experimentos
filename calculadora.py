import time
import sys
print("veamos si funciona la calculadora. ¿Cuál es tu nombre?")
nombre = input("escribe tu nombre aquí")
if nombre == "":
    print("No puedes dejar el campo de texto vacío")
    sys.exit()
else:
    print("muy bien, " + nombre + ".")
print("selecciona una opción")
x = int(input("¿qué quieres hacer. 1 para sumar, 2 para multiplicar y 3 para dividir"))
if x ==1:
    print("bien, vamos a sumar")
    suma = int(input("dame el primer valor"))
    suma2 = int(input("dame el segundo valor"))
    rs = suma + suma2
    print("el resultado es: ", rs)
elif x ==2:
    print("multipliquemos, " + nombre + ".")
    multiplicación = int(input("ingresa el primer número"))
    multiplicación2 = int(input("ingresa el segundo número"))
    rm = multiplicación * multiplicación2
    print("el resultado es el siguiente: ", rm)
elif x ==3:
    print("bien " + nombre + ", dividamos")
    d = int(input("dame el primer número"))
    f = int(input("dame el segundo número"))
    rd = d / f
    print("El resultado es:", rd)
    print("muchas gracias por usar el script.")
else:
    print(" no sé que hiciste pero eso no se puede")
time.sleep(2)