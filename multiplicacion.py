def multiplicacion():
    n1=int(input("ingresa primer número"))
    n2=int(input("ingresa segundo número"))
    resultado =n1 * n2
    print(f"el resultado es {resultado}")
def final():
    print("adiós!")
#Llamado a las funciones
for x in range(3):
    multiplicacion()
final()