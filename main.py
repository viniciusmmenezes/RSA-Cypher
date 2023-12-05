import hashlib
import sys
from random import randrange, getrandbits
from complement import Compl
from rsa import Rsa

sys.setrecursionlimit(1500)


#Converte uma lista para string
def convert_list_to_string(org_list):
  return ''.join([str(elem) for elem in org_list])


print('Rodando o Algoritmo RSA...\n')

#Miller-rabin
key_dict = Rsa.generatekeys()
e = key_dict["e"]
d = key_dict["d"]
n = key_dict["n"]

#Plaintext
file_encrypt = open('teste.txt', 'r', encoding='utf-8')
message = file_encrypt.read()
print("Plaintext: %s" % message)

#Calculando o hash do Plaintext
init = hashlib.sha3_512(message.encode())
hash_message = init.hexdigest()
print("\n\nHash do plaintext : %s" % hash_message)

#Cifrando a mensagem
cypher_str = Rsa.encryptRSA(message, e, n)
print("\nO Ciphertext: %s" % convert_list_to_string(cypher_str))

#Decifrando a mensagem
message = Rsa.decryptRsa(cypher_str, n, d)
str_message = convert_list_to_string(message)
print("\nA mensagem decifrada: %s" % str_message)

#Calculando o hash da mensagem decifrada
hash_decypher = hashlib.sha3_512()
hash_decypher.update(str_message.encode())
print("\n\nHash da mensagem decifrada: %s" % hash_decypher.hexdigest())

file_encrypt.close()

if (hash_message == hash_decypher.hexdigest()):
  print("\n\nCongratulations!\n")
  print("O hash do plaintext bate com o da mensagem decifrada!\n")
else:
  print("\n\nOps, algo deu errado!\n")


