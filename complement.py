class Compl:


  #algoritmo Euclidean mdc ou gdc
  def mdc(a, b):
    if b == 0:
      return a
    else:
      return Compl.mdc(b, a % b)

  #retorna o mdc coeficiente de a e de b
  def mod_inverse(a, b):
    x1, x2 = 0, 1
    y1, y2 = 1, 0

    while (b != 0):
      quotient = a // b
      a, b = b, a - quotient * b
      x2, x1 = x1, x2 - quotient * x1
      y2, y1 = y1, y2 - quotient * y1

    return a, x2, y2