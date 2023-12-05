# Trabalho-RSA
Trabalho 2 realizado para a UnB, matéria de segurança de dados com o professor João gondim

# gerador e verificador de assinaturas RSA em arquivos.

# Parte I: Geração de chaves
## 1. Geração de chaves (p e q primos com no mínimo de 1024 bits)
# Parte II: Cifra simétrica
## 1. Geração de chaves simétrica
## 2. Cifração simétrica de mensagem (AES modo CTR),
# Parte III: Geração da assinatura
## 1. Cálculo de hashes da mensagem em claro (função de hash SHA-3)
## 2. Assinatura da mensagem (cifração do hash da mensagem usando OAEP)
## 3. Formatação do resultado (caracteres especiais e informações para verificação em BASE64)
# Parte IV: Verificação:
## 1. Parsing do documento assinado e decifração da mensagem (de acordo com a formatação usada, no caso BASE64)
## 2. Decifração da assinatura (decifração do hash)
## 3. Verificação (cálculo e comparação do hash do arquivo)

# documento

https://docs.google.com/document/d/1MOO00MmtljWXo_VR6G1O7wtc-eFzeormwxGvg7vVeYk/edit?usp=sharing
# referencias 
https://sahandsaba.com/cryptography-rsa-part-1.html

http://koclab.cs.ucsb.edu/teaching/cren/project/2018/Adamczyk+Magnussen.pdf

https://medium.com/blue-space/improving-the-security-of-rsa-with-oaep-e854a5084918

https://fdocumentos.tips/document/rsa-oaep-rsa-o-seu-algoritmo-utiliza-o-conceito-de-criptografia-de-chave-publica-introduzido-por-diffie-hellman-e-baseado-no-problema-da-factorizacao.html

https://xilinx.github.io/Vitis_Libraries/security/2020.1/guide_L1/internals/ctr.html