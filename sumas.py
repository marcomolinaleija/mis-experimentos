import time
x = input("hola, ¿Cuál es tu nombre?")
#Imprimimos el mensaje que se mostrará en pantalla con el nombre del usuario. Para ello escribimos la función Print, seguido de una apertura de paréntesis y también una apertura de comillas. Ingresamos el texto que queremos que se muestre en pantalla. Por ejemplo, hola. seguido de eso cerramos las comillas, dejamos un espacio en blanco para escribir el nombre de la variable, pero antes hay que añadir el operador más. Añadimos el más y pasamos un espacio. Ahora sí ponemos el nombre de la variable. Ya que se ha escrito, dejamos otro espacio en blanco y volvemos a añadir el operador más. Otro espacio en blanco, y abrimos comillas para continuar imprimiendo mensajes en pantalla. Dejamos una coma seguido de un espacio para separar el nombre de lo siguiente que se escribirá. Aquí escribimos el texto que queramos. Por ejemplo, realizaremos una suma. ya que lo hayan escrito, cierran comillas para terminar con esa string. Por último cierran el paréntesis. pero es mucho texto, miremos en código...
print("Hola " + x + ", realizaremos una suma")
#Ahora añadimos las variables, declarando que serán de dato Int(entero)
dígito_1 = int(input("Escribe el primer valor"))
dígito_2 = int(input("Ahora el valor 2."))
#Hacemos la suma de las 2 variables, creando otra variable llamada resultado:
resultado = dígito_1 + dígito_2
#Ahora sí, imprimimos el resultado en pantalla:
print(x + ", El resultado de la suma es el siguiente: ", resultado)
time.sleep(2)