import sys
from random import randrange, getrandbits
from complement import Compl

sys.setrecursionlimit(1500)


class Rsa:

  # Teste de primalidade de Miller-Rabin
  def isPrime(value, k=128):
    if (value <= 1) or (value % 2 == 0):
      return False
    if (value == 2) or (value == 3):
      return True
    s = 0
    num = value - 1
    while num & 1 == 0:
      s += 1
      num //= 2
    for _ in range(k):
      numRandom = randrange(2, value - 1)
      result = pow(numRandom, num, value)
      if result != 1 and result != value - 1:
        j = 1
        while j < s and result != value - 1:
          result = pow(result, 2, value)
          if result == 1:
            return False
          j += 1
        if result != value - 1:
          return False
    return True

  def generatePossiblePrime(length):
    prime = getrandbits(length)
    prime |= (1 << length - 1) | 1
    return prime

  def generatePublicKey(length=1024):
    prime = 4
    while not Rsa.isPrime(prime, 128):
      prime = Rsa.generatePossiblePrime(length)
    return prime

  def chooseRandomE(totient):
    while (True):
      e = randrange(2, totient)
      if (Compl.mdc(e, totient) == 1):
        return e

  def generatekeys():
    prime1 = Rsa.generatePublicKey()
    prime2 = Rsa.generatePublicKey()
    #Escrever os primos no arquivo txt
    fo = open('keys/primos.txt', 'w')
    fo.write(str(prime1) + '\n')
    fo.write(str(prime2) + '\n')
    fo.close()

    resultMult = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)

    e = Rsa.chooseRandomE(totient)
    mdc, a, y = Compl.mod_inverse(e, totient)

    if a < 0:
      d = a + totient
    else:
      d = a
    # Escrever a chave publica no txt
    f_public = open('keys/chave_publica.txt', 'w')
    f_public.write(str(resultMult) + '\n')
    f_public.write(str(e) + '\n')
    f_public.close()
    # Escrever a chave privada no txt
    f_private = open('keys/chave_privada.txt', 'w')
    f_private.write(str(resultMult) + '\n')
    f_private.write(str(d) + '\n')
    f_private.close()
    key_dict = {'n': resultMult, 'e': e, 'd': d}
    return key_dict

  # Função para criptografar

  def encryptRSA(message, e, n):
    size = len(message)
    i = 0
    cypher_str = []
    while (i < size):
      letter = message[i]
      k = ord(letter)
      c = pow(k, e, n)
      cypher_str.append(c)
      i += 1
    return cypher_str

  # Função para descriptografar

  def decryptRsa(cypher_str, n, d):
    size = len(cypher_str)
    i = 0
    decypher_str = []
    while (i < size):
      r = pow(int(cypher_str[i]), d, n)
      letter = chr(r)
      decypher_str.append(letter)
      i += 1
    return decypher_str
