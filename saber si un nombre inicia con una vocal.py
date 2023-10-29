nick=input("ingresa tu nombre")
if nick[0]=="a" or nick[0]=="e" or nick[0]=="i" or nick[0]=="o" or nick[0]=="u":
    print(f"tu nombre inicia con una bocal: la bocal es: {nick[0]}")
else:
    print(f"tu nombre no inicia con una bocal. la primer letra de tu nombre es: {nick[0]}")