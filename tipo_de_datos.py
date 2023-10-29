#En el siguiente script, se tratará el cómo saber de qué tipo de dato es la variable a utilizar. Tenemos la variable número1, y en la línea inferior, imprimimos el número que está dentro de esa variable, el cual es 2. Después, para saber que tipo de variable se utiliza, colocamos otro comando print, seguido de una apertura de paréntesis. Aquí hacemos un llamado a la función type. Abrimos paréntesis para indicarle el nombre de la variable de la que queremos saber su tipo. Cuando se haya escrito, hacemos doble cierre de paréntesis. uno para cerrar la función type, y el otro para cerrar la función print
número1 =2
type(número1)
print(número1)
print(type(número1))
verdadero_falso = 3
if verdadero_falso == 3:
    print("verdadero_falso es igual a 3")
else:
    print("verdadero_falso no es 3")