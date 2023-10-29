import time
print("Hola, convirtamos números a letras. O sea el número escrito pues")
num_uno = int(input("¿Cual es el número que quieres convertir?"))
if num_uno == 1:
    print("el número es uno")
elif num_uno == 2:
    print("el número es dos")
elif num_uno == 3:
    print("el número es tres")
elif num_uno == 4:
    print("el número es cuatro")
elif num_uno == 5:
    print("el número es Cinco")
else:
    print(" No, solo se puede hasta el 5")
    print("adiós")
time.sleep(2)