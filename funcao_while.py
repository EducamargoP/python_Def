"""""
Exercício 4 – Função com While: Adivinhe o Número
Escreva uma função chamada adivinhe() que:

Gera um número secreto entre 1 e 10.

Pede para o usuário tentar adivinhar.

Usa while para repetir até acertar.

Informa se o palpite é maior ou menor que o número secreto.

🎯 Objetivo: aplicar while em um contexto interativo e divertido.
"""

from random import randint

robo = randint(0,10)
print("JOGO DE ADIVINHAR!")
while True:
    num = int(input("DIGA NUMERO:"))
    if num == robo:
        print("VOCE ACERTOU! PARABENS")
        break
    elif num < robo:
        print("TENTE NOVAMENTE, NUMERO MAIOR!")
    elif num > robo:
        print("TENTE NOVAMENTE, NUMERO MENOR!")
