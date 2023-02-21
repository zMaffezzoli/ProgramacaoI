import math

class Poligono:
    def __init__(self):
        self.__pontos = []

    def __str__(self):
        string = ""
        for i in self.__pontos:
            string += f"{str(i)} "
        return f"{string}"

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos
    
    def addPonto(self, ponto):
        self.__pontos.append(ponto)

    def perimetro(self):
        soma = 0
        controle = len(self.__pontos)

        for i in range(controle):
            x1 = self.__pontos[(i+1)%controle].x
            y1 = self.__pontos[(i+1)%controle].y
            x0 = self.__pontos[i].x
            y0 = self.__pontos[i].y
            soma += math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

        return f"O perímetro do polígono convexo formado é de: {soma}"

    def area(self):
        soma = 0
        controle = len(self.__pontos)

        for i in range(controle):
            x1 = self.__pontos[(i+1)%controle].x
            y1 = self.__pontos[(i+1)%controle].y
            x0 = self.__pontos[i].x
            y0 = self.__pontos[i].y
            soma += (x0*y1 - x1*y0)

        return f"A área do polígono convexo formado é de: {soma/2}"