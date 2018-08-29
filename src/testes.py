import jogovelha
import sys

erroInicialisar = False
jogo = jogovelha.inicialisar()
if len(jogo) != 3:
    erroInicialisar = True
else:
    for linha in jogo:
        if len(linha) !=3:
            erroInicialisar = True
        else:
            for elemento in linha:
                if elemento != ".":
                    erroInicialisar = True
if erroInicialisar:
    sys.exit(1)
else:
    sys.exit(0)
