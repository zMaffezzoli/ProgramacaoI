class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = str(nome)
        self.__cpf = str(cpf)
        self.__salario = float(salario)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def getBonificacao(self):
        self.__salario = self.__salario*1.10
        return self.__salario