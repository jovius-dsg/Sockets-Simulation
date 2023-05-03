import random
import os
import time

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        return self.meu_ipv4()
        
    def meu_ipv4(self):

        octeto1 = random.randint(0, 255)
        octeto2 = random.randint(0, 255)
        octeto3 = random.randint(0, 255)
        octeto4 = random.randint(0, 255)
        
        endereco_ipv4 = f"{octeto1}.{octeto2}.{octeto3}.{octeto4}"
        letra = (f'Bem vindo, {self.nome}! IP: {endereco_ipv4}')    
        for letra in letra:
            print(letra, end = '', flush = True)
            time.sleep(0.2)
        

        