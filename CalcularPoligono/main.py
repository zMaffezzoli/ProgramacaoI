from ponto import *
from poligono import *

# ===== Criar ponto =====
ponto1 = Ponto(1, 1)
ponto2 = Ponto(5, 1)
ponto3 = Ponto(1, 4)

# ===== Utiliza função str =====
print(ponto1)
print(ponto2)
print(ponto3,"\n")

# ===== Criar polígono =====
poligono = Poligono()

# ===== Adicionar pontos ao polígono =====
poligono.addPonto(ponto1)
poligono.addPonto(ponto2)
poligono.addPonto(ponto3)

# ===== Utiliza função str =====
print(poligono, "\n")

# ===== Perímetro do polígono =====
print(poligono.perimetro())
print(poligono.area())