import numpy
import math


def calcularProbabilidad(mu, x):
  """
  Función que calcula la probabilidad de Poisson
  mu: media o valor esperado de X. Debe ser mayor a 0
  x: número de ocurrencias (valor de la variable aleatoria)
  """
  e = math.e
  return (pow(e,-mu)*pow(mu, x))/math.factorial(x) 

def seleccionarTipoCalculo(tipo_calculo):
  print("Seleccione el tipo de cálculo:")

  for key, value in tipo_calculo.items():
    print(f"{key}. {value}")

  opcion = int(input("Ingrese el número correspondiente al tipo de cálculo: "))

  if opcion not in tipo_calculo:
    raise ValueError("Opción inválida. Por favor, seleccione una opción válida.")
  

  return opcion


def calcular_probabilidad_por_tipo(mu, x, opcion):
  """
  Devuelve la probabilidad según la opción:
  1: X = x
  2: X < x
  3: X ≤ x
  4: X > x
  5: X ≥ x
  """
  probabilidad = 0.0

  if opcion == 1:
      probabilidad = calcularProbabilidad(mu, x)
  elif opcion == 2:
      for i in range(0, x):
          probabilidad += calcularProbabilidad(mu, i)
  elif opcion == 3:
      for i in range(0, x + 1):
          probabilidad += calcularProbabilidad(mu, i)
  elif opcion == 4:
      for i in range(0, x + 1):
          probabilidad += calcularProbabilidad(mu, i)
      probabilidad = 1 - probabilidad
  elif opcion == 5:
      for i in range(0, x):
          probabilidad += calcularProbabilidad(mu, i)
      probabilidad = 1 - probabilidad
  else:
      raise ValueError("Opción de cálculo desconocida")

  return probabilidad

def poisson(media, ocurrencias):
  """
  f(x) = P(X = x) = (e^(-μ) * μ^x) / x!
  media: μ o valor esperado de X. Debe ser mayor a 0
  e: base de los logaritmos naturales. 
  x: número de ocurrencias (valor de la variable aleatoria)
  """
  mu = media
  x = ocurrencias

  tipo_calculo = {1:"X = x", 2:"X < x", 3:"X ≤ x", 4:"X > x", 5:"X ≥ x"}

  if mu < 0:
    raise ValueError("El valor de mu (media) debe ser mayor a 0")
  
  opcion = seleccionarTipoCalculo(tipo_calculo)
  probabilidad = 0.0
  probabilidad = calcular_probabilidad_por_tipo(mu, x, opcion)

  print(f"La probabilidad {tipo_calculo[opcion]}: {(probabilidad * 100):.2f}%")

poisson(media=8, ocurrencias=10)

