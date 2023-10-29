#se crea la primer función para mostrar mensajes en pantalla
def show_mesage(mensaje):
    print(mensaje)
#se crea la función para la suma de números
def suma():
    x=int(input("ingresa el primer valor"))
    c=int(input("ingresa el segundo valor"))
    suma=x+c
    print(f"la suma de los 2 números es la siguiente: {suma}")
#llamado a las funciones
show_mesage("hola. vamos a realizar una suma utilizando funciones")
suma()