"""
O que o desafio pede?
Dada uma lista de inteiros:

Calcular a proporção de números positivos, negativos e zeros.

Imprimir cada proporção com 6 casas decimais, uma por linha.

"""

lista = [-4, 3, -9, 0, 4]

def plusMinus(arr):
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    print(f"{pos / total:.6f}")
    print(f"{neg / total:.6f}")
    print(f"{zero / total:.6f}")

# Leitura da entrada como o HackerRank espera
n = int(input())
arr = list(map(int, input().split()))
plusMinus(arr)






