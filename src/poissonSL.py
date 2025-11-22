import math

def calcularProbabilidad(mu: float, x: int) -> float:
  """
  Función que calcula la probabilidad de Poisson
  """
  e = math.e
  if mu < 0:
    raise ValueError("mu debe ser > 0")
  if x < 0:
    raise ValueError("x debe ser entero >= 0")

  return (pow(e,-mu)*pow(mu, x))/math.factorial(x) 

def calcular_probabilidad_por_tipo(mu: float, x: int, opcion: int) -> float:
  """Calcula la probabilidad solicitada según la opción:

  1: P(X = x)
  2: P(X < x)
  3: P(X ≤ x)
  4: P(X > x)
  5: P(X ≥ x)

  """
  if mu < 0:
    raise ValueError("El valor de mu (media) debe ser mayor o igual a 0")
  if x < 0:
    raise ValueError("x debe ser >= 0")

  probabilidad = 0.0

  if opcion == 1:
    # P(X = x)
    probabilidad = calcularProbabilidad(mu, x)

  elif opcion == 2:
    # P(X < x) 
    for i in range(0, x):
      probabilidad += calcularProbabilidad(mu, i)

  elif opcion == 3:
    # P(X ≤ x)
    for i in range(0, x + 1):
      probabilidad += calcularProbabilidad(mu, i)

  elif opcion == 4:
    # P(X > x) = 1 - P(X ≤ x)
    for i in range(0, x + 1):
      probabilidad += calcularProbabilidad(mu, i)
    probabilidad = 1.0 - probabilidad

  elif opcion == 5:
    # P(X ≥ x) = 1 - P(X < x)
    for i in range(0, x):
      probabilidad += calcularProbabilidad(mu, i)
    probabilidad = 1.0 - probabilidad

  else:
    raise ValueError("Opción de cálculo invalida")

  return probabilidad

__all__ = [
  "calcularProbabilidad",
  "calcular_probabilidad_por_tipo",
]


