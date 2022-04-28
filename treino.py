class Carro:
    def __init__(self, marca, nome, cor, ano):
        self.marca = marca
        self.nome = nome
        self.cor = cor
        self.ano = ano

    def ligar(self):
        print('O carro está ligando!')

    def desligar(self):
        print('O carro está desligado')


