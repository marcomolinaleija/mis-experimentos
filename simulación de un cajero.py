import time
def validar_cuenta(num_cuenta):
    if not num_cuenta.isdigit():
        return False
    elif len(num_cuenta) != 16:
        return False
    else:
        return True
        
saldo = 10000
def bienvenido(mensaje):
    print(mensaje)

def cajero_automático():
    global saldo
    nip =input("Ingresa tu NIP para acceder al cajero")
    
    print("validando...")
    
    time.sleep(2)
    print("Verificación exitosa. A continuación se muestra en pantalla la cantidad actual de tu saldo")
    print(f"El saldo de tu cuenta es de: {saldo} pesos.")

    print("Elige qué quieres hacer")
    print("Presiona la tecla 1 para retirar dinero")
    print("Presiona la tecla 2 para ingresar dinero")
    print("Presiona la tecla 3 para enviar dinero")

    opción = int(input("Ingresa la opción que desees"))
    if opción == 1:
        cantidad = int(input("¿Cuánto quieres retirar?"))
        if cantidad > saldo:
            print("No cuentas con dinero suficiente")
        else:
            print(f"Muy bien. Se retirarán {cantidad} pesos de tu cuenta (ten en cuenta que esto es irreversible)")
            saldo -= cantidad
            print("Retirando: por favor, espera un momento")
            time.sleep(3)
            print("Operación exitosa")
            print(f"Con el retiro, tu saldo actual es de: {saldo} pesos")
            print("Muchas gracias por utilizar este cajero")
            time.sleep(1)

    if opción == 2:
        ing = int(input("¿Cuánto dinero quieres ingresar?"))
        saldo += ing
        print("Por favor espera...")
        time.sleep(1)
        print("Operación exitosa")
        print(f"Muy bien. Se han ingresado {ing} pesos de manera correcta. Tu saldo actual es de: {saldo} pesos")
        print("Muchas gracias por utilizar este cajero")
        time.sleep(2)

    if opción == 3:
        num_cuenta = input("Por favor ingresa el número de cuenta a la cual quieres enviar dinero (16 dígitos): ")
        if validar_cuenta(num_cuenta):
            print(f"Aquí está el número que ingresaste: {num_cuenta}")
            cantidad_a_enviar = int(input("¿Cuánto dinero vas a enviar?"))
            if cantidad_a_enviar <= saldo:
                print(f"Muy bien. Se enviarán {cantidad_a_enviar} pesos a la cuenta:{num_cuenta}: ¿Seguro que quieres continuar?")
                confirmación = input("Escribe 'si' para continuar o 'no' para denegar la operación: ")
                if confirmación == 'si':
                    print("Muy bien")
                    saldo -= cantidad_a_enviar
                    print("enviando...")
                    time.sleep(1)
                    print(f"Al enviar la cantidad, tu saldo actual ahora es de: {saldo}")
                else:
                    print("Puto pobre")
bienvenido("este cajero está en fase de prueba, no lo hateen")
cajero_automático()