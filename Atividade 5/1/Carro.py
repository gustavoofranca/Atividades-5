class Carro():
    def __init__(self, modelo, ano):
        self._modelo = modelo
        self._ano = ano

    def acao(self):
        print(f'{self._modelo}, {self._ano} faz burnout')


