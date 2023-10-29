nicks=[]
edades=[]
for x in range(5):
    nick=input("ingrese el nombre de la persona")
    nicks.append(nick)
    ed=int(input("ingrese la edad"))
    
    edades.append(ed)
print("las personas mayores de edad son:")
for x in range(5):
    if edades[x]>=18:
        print(nicks[x])