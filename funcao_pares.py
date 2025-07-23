""""
Exercício 3 – Função: Soma de Pares
Crie uma função chamada soma_pares(lista) que:

Recebe uma lista de números.

Retorna a soma de todos os números pares.

Utilize um loop for dentro da função.
"""

def soma_pares(lista):
    soma = 0
    par = []
    impar = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
            soma += i

        elif i % 2 == 1:
            impar.append(i)

    print(par)
    print(impar)
    return f'SOMA DOS PARES {soma}'

numeros = []

for num in range(5):
    num = int(input(F'DIGA NUMERO {num+1}: '))
    numeros.append(num)
print(soma_pares(numeros))




















