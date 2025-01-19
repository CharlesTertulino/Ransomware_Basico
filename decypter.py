## IMPORTANDO BIBLIOTECAS
import os
import pyaes

## ABRINDO O ARQUIVO CRITOGRAFADO
nome_arquivo = "alvo.txt.ransomwaretroll"
arquivo = open(nome_arquivo, "rb")
dados_arquivo = arquivo.read()
arquivo.close()

## CHAVE DE DESCRITOGRAFIA
chave = "exponencialmente"
aes = pyaes.AESModeOfOperationCTR(chave)
dados_descripto = aes.decrypt(dados_arquivo)

## DESTRUINDO ARQUIVO CRIPTOGRAFADO
os.remove(nome_arquivo)

## CRIANDO ARQUIVO DESCRIPTOGRAFADO
novo_arquivo = "alvo.txt"
novo_arquivo = open(f"{novo_arquivo}", "wb")
novo_arquivo.write(dados_descripto)
novo_arquivo.close()