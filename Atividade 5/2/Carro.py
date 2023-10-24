class Carro():
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano

    def acao(self):
        print(f'{self.__modelo}, {self.__ano} acelerando!!')
