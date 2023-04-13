import random
import os

caminho = os.path.dirname(os.path.abspath(__file__))
arquivotxt = os.path.join(caminho, "words.txt")

# Função para sortear a palavra da forca
def palavra_forca():
    num = random.randint(0, 39)
    arquivo = open(arquivotxt, 'r')
    ler = arquivo.readlines()
    palavra = ler[num][:-1]
    arquivo.close()
    return palavra