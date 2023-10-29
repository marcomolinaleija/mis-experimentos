import time
nick=input("Ingresa tu nombre")
while nick == "":
    nick=input("No puedes dejar el campo de nombre sin caracteres. Ingresa tu nombre ptm")
print(f"Hola {nick}, ¿Como estás?")
respuesta=input("Respóndeme")
print(f"Me alegro que te encuentres {respuesta}, {nick}. Pero me vale vrg, mejor sigamos con el código\n")
print("Vamos a comparar cuál es el número mas grande pero ahora introduciendo más valores\n")
n1=int(input("Ingresa el primer número, entero"))
n2=int(input("Ingresa el segundo número"))
n3=int(input("Ingresa el terser número"))
n4=int(input("Ingresa el cuarto número"))
n5=int(input("Ingresa el quinto número"))
print(f"Muy bien, {nick}\n")
print(f"Hagamos un recorrido por los números que has ingresado: primero: {n1}. segundo: {n2}. tersero: {n3}. cuarto: {n4}. quinto: {n5}")
time.sleep(2)
print("Ahora, hagamos las comparaciones\n")
print("Por favor, espera...")
time.sleep(3)
print(f"Listo {nick}. Se han realizado las comparaciones. A continuación te muestro el número mayor")
time.sleep(1)
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f"Tras una serie de comparaciones, el número más grande es: {n1}")
else:
    if n2 > n3 and n2 > n4 and n2 > n5:
        print(f"Tras una serie de comparaciones, el número mayor es: {n2}")
    else:
        if n3 > n4 and n3 > n5:
            print(f"Tras una serie de comparaciones, el número más grande es el {n3}")
        else:
            if n4 > n5:
                print(f"Tras una serie de comparaciones, el número más grande es el {n4}")
            else:
                print(f"El número más grande es el {n5}")
time.sleep(2)