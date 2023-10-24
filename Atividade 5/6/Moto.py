from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, tipo, velocidade):
        super().__init__(tipo, velocidade)

    def passaRadar(self):
        print(f'{self._tipo} passou no radar a {self._velocidade} km/h')
