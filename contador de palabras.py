def contar_palabras(texto):
  """
  Cuenta la cantidad de palabras en un texto.

  Args:
    texto: El texto a contar.

  Returns:
    La cantidad de palabras en el texto.
  """

  palabras = texto.split()
  return len(palabras)


if __name__ == "__main__":
  texto = input("Introduce un texto: ")
  cantidad_palabras = contar_palabras(texto)
  print(f"El texto contiene {cantidad_palabras} palabras.")
