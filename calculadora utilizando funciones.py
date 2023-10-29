def presentación():
    print("hola. esta es una calculadora diferente en cuestión código")
def calculadora():
    nick=input("escribe tu nombre")
    while nick == "":
        nick=input("por favor ingresa tu nombre")
    print(f"hola, {nick}")
    print("calculemos")
    print("¿Qué quieres hacer?")
    print("preciona el signo + para sumar o el signo -(guión) para restar")
    opción=input("elije la opción deseada")
    if opción == "+":
        x=int(input("ingresa el primer número"))
        x +=int(input("ingresa el segundo número"))
        print(f"muy bien, {nick}. el resultado de la operación es: {x}")
    elif opción == "-":
        x=int(input("ingresa el primer número"))
        x -=int(input("ingresa el segundo número"))
        print(f"la operación dio el número {x}")
    else:
        print(f"ptm {nick}, esa opción no está disponible")
presentación()
calculadora()