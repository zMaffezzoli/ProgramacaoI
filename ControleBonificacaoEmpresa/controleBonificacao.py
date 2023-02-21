from decimal import Decimal

class ControleDeBonificacoes:
    def __init__(self):
        self.__totalBonificacao = Decimal(0)

    @property
    def totalBonificacao(self):
        return self.__totalBonificacao

    @totalBonificacao.setter
    def totalBonificacao(self, totalBonificacao):
        self.__totalBonificacao = totalBonificacao

    def registra(self, sujeito):
        self.__totalBonificacao += Decimal(sujeito)

    def getTotalBonificacoes(self):
        return Decimal(self.__totalBonificacao)