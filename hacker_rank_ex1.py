"""
FizzBuzz - Desafio proposto pelo HackerRank

Este programa imprime uma sequência de valores de 1 até 10, seguindo as regras:

- Se o número for múltiplo de 3 e 5, imprime "FizzBuzz"
- Se for múltiplo de apenas 3, imprime "Fizz"
- Se for múltiplo de apenas 5, imprime "Buzz"
- Caso contrário, imprime o próprio número

A saída é exibida linha por linha.

Exemplo:
Para n = 5, a saída será:
1
2
Fizz
4
Buzz

Fonte: HackerRank
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista:
    if numero % 3 == 0 and numero % 5 ==0:
        print('FIZZBUZZ')
    elif numero % 3 == 0:
        print('FIZZ')
    elif numero % 5 == 0:
        print('BUZZ')
    else:
        print(numero)
