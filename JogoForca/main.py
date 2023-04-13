from general.colors import *
from general.generateWord import *

palavra_escolhida = palavra_forca()
digitadas = []
chances = 5

# Abertura do jogo
print(f"{amarelo}+{azul}-"*30)
print((vermelho),"JOGO DA FORCA".center(60))
print(f"{amarelo}+{azul}-"*30, (reset))
print((ciano),(len(palavra_escolhida) * "_ ").center(60), (reset))

while True:
    inserir_letra = input(f"\n{branco}Digite uma letra: ")
    print(reset)

    if len(inserir_letra) > 1:
        print(f"{vermelho}Erro!! Apenas uma letra por vez{reset}")
        continue

    elif inserir_letra.isalpha() == False:
        print(f"{vermelho}Erro!! Apenas letras são permitidas!{reset}")
        continue

    else:
        inserir_letra = inserir_letra.upper()
        if inserir_letra not in digitadas:
            digitadas.append(inserir_letra)
        else:
            print(f"{vermelho}Letra repetida!{reset}")
            continue

    secreta = ""

    for i in palavra_escolhida:
        if i in digitadas:
            secreta += i
        else:
            secreta += "_"

    print(f"{ciano}A palavra está assim: {magenta}{secreta}{reset}")

    if inserir_letra not in palavra_escolhida:
        chances -= 1

    print(f"{amarelo}\nVocê tem {chances} chances!{reset}")
    print(f"{verde}\nLetras utilizadas: {reset}", end="",)

    for i in digitadas:
        print(verde, i, end =",")

    if chances == 0:
        print(f"{vermelho}\n\nVocê perdeu! A palavra era {palavra_escolhida}{reset}")
        break

    elif secreta == palavra_escolhida:
        print((ciano),"\n\nVocê venceu o jogo, parabéns!",(reset))
        break