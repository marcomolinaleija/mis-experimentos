import time
num1=int(input("ingresa el primer número"))
print(f"bien, qué quieres hacer con el número {num1}?")
print("escribe lo que quieres. presiona el operador + para una suma, el operador -(guión) para una resta, o el operador * para una multiplicación\n")
selec=input("ingresa aquí")
if selec == "+" or selec == "sumar" or selec == "mas":
    num2=int(input("ingresa el segundo número"))
    resultado =num1 + num2
print(f"el resultado es. {resultado}")
time.sleep(1)