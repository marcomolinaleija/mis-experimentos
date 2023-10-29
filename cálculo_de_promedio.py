import time
print("Hola. Vamos a calcular un promedio")
nombre = input("¿Cuál es tu nombre? ")
print("Muy bien, ", nombre, ": comencemos:")
química = int(input("¿Cuál fue tu calificación en química? "))
inglés = int(input("¿Cuál fue tu calificación final en inglés? "))
cálculo = int(input(nombre +  ", ¿Cuál fue tu calificación en cálculo?"))
promedio = (química + inglés + cálculo) / 3
promedio = int(promedio)
if promedio >= 6:
    print("felisidades, ", nombre, "has aprobado con un promedio de", promedio)
print("finalizado")
time.sleep(2)