import time
def retornar_mayor(n1,n2):
    if n1 > n2:
        mayor=n1
    else:
        mayor=n2
    return mayor
#cargar números
valor1=int(input("ingresa un valor"))
valor2=int(input("ingresa otro valor"))
print(retornar_mayor(valor1,valor2))
time.sleep(1)