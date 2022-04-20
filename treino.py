class Carro():
    def __init__(self, marca, nome, cor, ano):
        self.marca = marca
        self.nome = nome
        self.cor = cor
        self.ano = ano

    def Ligar(self):
        print('O carro está ligando!')

    def Desligar(self):
        print('O carro está desligado')


