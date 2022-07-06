# Simulador de Dado 
# Simular o uso de um dado, gerando uma valor de 1 ate 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado?"
        
