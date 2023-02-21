import random

# Função para sortear a palavra da forca
def palavra_forca():
    num = random.randint(0, 39)
    arquivo = open('words.txt', 'r')
    ler = arquivo.readlines()
    palavra = ler[num][:-1]
    arquivo.close()
    return palavra