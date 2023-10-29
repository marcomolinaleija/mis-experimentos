import time
numuno=int(input("ingresa el primer número"))
numdos=int(input("ingresa el segundo número"))
numtres=int(input("ingresa el tercer número"))
if numuno>numdos and numuno>numtres:
    print(f'el número {numuno} es el más grande')
else:
    if numdos>numtres:
        print(f'el número {numdos} es el más grande')
    else:
        print(f'el número {numtres} es el más grande')
time.sleep(2)