def mensaje(msg):
    print(msg)
def ALTC():
    persona1=float(input("ingresa la estatura de la primer persona"))
    nombre=input("ingresa su nombre")
    persona2=float(input("ingresa la estatura de la segunda persona"))
    nombre2=input("ingresa su nombre")
    if persona1 > persona2:
        print(f"la persona más alta es {nombre}")
    else:
        print(f"la persona más alta es {nombre2}")
mensaje("calcularemos quién es la persona con la mayor estatura")
ALTC()