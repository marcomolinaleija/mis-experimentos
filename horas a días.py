def main():
  # Solicitamos las horas al usuario
  hora = int(input("Ingresa las horas: "))

  # Si las horas son superiores a 24, calculamos los días
  if hora >= 24:
    dias = hora // 24
    horas_restantes = hora % 24
    print("Han pasado {} días y {} horas".format(dias, horas_restantes))
  else:
    # Si las horas son inferiores o iguales a 24, solo mostramos las horas
    print("Las horas ingresadas son: {} horas".format(hora))

if __name__ == "__main__":
  main()
