"""
Crie um jogo de adivinhação de número em que o programa gere aleatoriamente um número entre 1 e 10.
O usuário deverá tentar adivinhar o número até acertar.
A cada tentativa, o programa deve informar se o chute foi alto, baixo ou correto.
"""

from random import randint

robo = randint(0, 10)
while True:
    print("NUMERO DE O A 10")
    num = int(input("Diga um numero:"))
    if num == robo:
        print("VOCE ACERTOU")
    elif num < robo:
        print(' QUASE TENTE MAIS ALTO!')
    elif num > robo:
        print('QUASE TENTE MAIS BAIXO!')

