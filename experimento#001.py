import os
import time

print("¡Hola!")
app = input("escribe la aplicación que quieres que se ejecute")
test = input("Escribe algo aquí, tu nombre, por ejemplo: ")
if test == "":
    print("no")

print(f"Hola, {test}.")

print("Solo es una prueba.")

edad = input("Escribe tu edad: ")
print(f"Así que tienes {edad} años. Eso es genial, {test}.")

print(f"Ahora, {test}, ejecutemos {app}. ¿Estás listo?")
x = input("Responde (sí/no): ")

if x.lower() == 'si':
    print("espera 5 segundos...")
    time.sleep(5)
    os.system(os.path.join(os.getcwd(), app))
    time.sleep(5)
