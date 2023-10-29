preguntas_totales=int(input("¿Cuántas preguntas se realizaron?"))
preguntas_correctas=int(input("¿Cuántas preguntas respondió de manera correcta?"))
porcentaje=preguntas_correctas * 100 / preguntas_totales
if porcentaje>=90:
    print("nivel máximo")
else:
    if porcentaje>=75:
        print("nivel medio")
    else:
        if porcentaje>=50:
            print("nivel regular")
        else:
            print("fuera de nivel")