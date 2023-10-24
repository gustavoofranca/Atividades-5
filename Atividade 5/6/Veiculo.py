class Veiculo():
    def __init__(self, tipo, velocidade):
        self._tipo = tipo
        self._velocidade = velocidade

    def acelerar(self):
        print(f'O veiculo {self._tipo }, acelerou e agora está a {self._velocidade + 25} km/h')

    def descricao(self):
        print(f'O veiculo {self._tipo }, de cor preta e sua velocidade máxima é de {self._velocidade} km/h')