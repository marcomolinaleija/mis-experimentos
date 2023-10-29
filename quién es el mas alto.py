import time

print("¿Quién es más alto?")
nombre1 = input("Ingresa el nombre de la primera persona: ")
edad1 = int(input("Ingresa la edad: "))
altura1 = float(input("Ingresa su altura: "))

print("Persona 2")
nombre2 = input("Ingresa el nombre: ")
edad2 = int(input("Ingresa la edad: "))
altura2 = float(input("Ingresa su altura: "))

if altura1 > altura2:
    print(f"La persona más alta es: {nombre1}: con una altura de {altura1}, y con {edad1} años de edad.")
else:
    print(f"La persona más alta es: {nombre2}: con una altura de {altura2}, y con {edad2} años de edad.")

time.sleep(3)
