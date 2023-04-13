from models.funcionario import *

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtdeGerenciados):
        super().__init__(nome, cpf, salario)
        self.__salario = float(salario)
        self.__senha = str(senha)
        self.__qtdeGerenciados = int(qtdeGerenciados)

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def qtdeGerenciados(self):
        return self.__qtdeGerenciados

    @qtdeGerenciados.setter
    def qtdeGerenciados(self, qtdeGerenciados):
        self.__qtdeGerenciados = qtdeGerenciados

    def getBonificacao(self):
        self.salario = self.salario*1.15
        return self.salario