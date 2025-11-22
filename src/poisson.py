import numpy
import math
"""

f(x) = P(X=x) : probabilidad de x ocurrencias en un intervalo.
media = μ o valor esperado de X. Debe ser mayor a 0
e: base de los logaritmos naturales. 

"""
def poisson(media, ocurrencias):
  e = math.e
  mu = media
  x = ocurrencias

  if mu < 0:
    raise ValueError("El valor de mu (media) debe ser mayor a 0")
  
  probabilidad = (pow(e,-mu)*pow(mu, x))/math.factorial(x) * 100

  print(f"La probabilidad es: {probabilidad:.2f}%")


poisson(media=-2, ocurrencias=5)