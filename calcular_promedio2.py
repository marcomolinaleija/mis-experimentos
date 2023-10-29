#Esto es casi el mismo código que el de cálculo de promedio, pero con condicionales compuestas
import time

print("hola, vamos a calcular tu promedio: ")

nombre =input("¿Cuál es tu nombre?")
print("hola, ", nombre, ", esperemos te haya ido bien. veamos...")
química = float(input("¿Cuál fue tu calificación final en química?"))
matemáticas = float(input("¿Cuál fue tu calificación final en matemáticas?"))
promedio = (química + matemáticas) / 2
if promedio >= 6:
    print("felicidades, " + nombre + ". has aprobado con un promedio de: ", promedio, ": adiós")
else:
    print("estás bien wey, ", nombre, ": tu promedio final es de: ", promedio)
time.sleep(2)