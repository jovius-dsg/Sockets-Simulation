import os
import time

from Cliente import *
from Servidor import *
from Funcoes import *

#Criando o cliente
def gerarCliente():
    x = input('Digite seu nome: ')
    cliente = Cliente(x)
    


#HandShake
frase1 = '[CLIENTE]: CONECTANDO'
frase2 = '[SERVIDOR]: CONEXÃO ESTABELECIDA'

#Protocolo
frase3 = '[CLIENTE]: ENVIANDO REQUISIÇÃO'
frase4 = '[CLIENTE]: DADOS RECEBIDOS'
frase5 = '[SERVIDOR]: ENVIANDO REQUISIÇÃO'
frase6 = '[SERVIDOR]: DADOS RECEBIDOS'
frase7 = '[SERVIDOR]: DESCONECTANDO'

def respostaServidorCliente(frase):
    os.system('cls') or None
    for letra in frase:
        print(letra, end = '', flush = True)
        time.sleep(0.05)

def Menu():
    os.system('cls') or None
    print("--- AÇÕES ---")
    print("LIST")
    print("VOTE")
    print("RANK")
    print("DISCONNECT")
    Acoes()
    

def Acoes():
    
    while True:
        inicio = input('Digite uma ação: ')

        match inicio:
                case "LIST":
                    respostaServidorCliente(frase3)
                    respostaServidorCliente(frase6)
                    respostaServidorCliente(frase5)
                    respostaServidorCliente(frase4)
                    List()

                case "VOTE":
                    respostaServidorCliente(frase3)
                    respostaServidorCliente(frase6)
                    respostaServidorCliente(frase5)
                    respostaServidorCliente(frase4)
                    Vote()

                case "RANK":
                    respostaServidorCliente(frase3)
                    respostaServidorCliente(frase6)
                    respostaServidorCliente(frase5)
                    respostaServidorCliente(frase4)
                    Ranked()

                case "EXIT":
                    respostaServidorCliente(frase7)
                    break

                case _:
                    respostaServidorCliente(frase7)
                    break    

