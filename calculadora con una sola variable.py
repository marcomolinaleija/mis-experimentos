import time
nick =input("Escribe tu nombre antes de continuar")
while nick == "":
    nick =input("por favor introduce tu nombre")
print(f'Hola {nick}, ¿cómo estás?')
print("Bienvenido/a a la calculadora con una sola variable \n")
print("Presiona uno para sumar \n")
print("Presiona 2 para restar \n")
print("Presiona 3 para multiplicar \n")
print("Presiona 4 para dividir \n")
print("Presiona 5 para una división entera \n")
print("Presiona 6 para elevar un número \n")
numero = int(input("Elige qué quieres hacer"))
if numero == 1:
    print("Bien, elegiste sumar")
    numero = int(input("Introduce el primer valor"))
    while numero <=-1:
        numero=int(input(f"no puedes introducir números negativos. por favor, {nick}, introduce un número mayor a 0"))
    numero += int(input("Introduce el valor 2"))

    print("El resultado de la suma es: ", numero)
    time.sleep(2)
elif numero == 2:
    print("Bien, elegiste restar \n")
    numero =int(input("introduce el primer valor"))
    numero -= int(input("Introduce el valor 2"))
    print("El resultado de la resta es: ", numero)
    time.sleep(2)
elif numero == 3:
    print("elegiste multiplicar \n")
    numero =int(input("Introduce el primer valor"))
    numero *= int(input("Introduce el valor 2"))
    print("El resultado de la multiplicación es: ", numero)
    time.sleep(2)
elif numero == 4:
    numero =int(input("Introduce el primer valor"))
    numero /= int(input("Introduce el valor 2"))
    print("El resultado de la divición es: ", numero)
    time.sleep(2)
elif numero == 5:
    numero =int(input("Introduce el primer valor"))
    numero //= int(input("Introduce el valor 2"))
    print("El resultado de la división entera es: ", numero)
    time.sleep(2)
elif numero == 6:
    numero =int(input("Introduce el primer valor"))
    numero **= int(input("Introduce el valor 2"))
    print("El resultado del exponente es: ", numero)
    time.sleep(2)
else:
    print("Esa opción no está disponible por ahora.")
    time.sleep(2)