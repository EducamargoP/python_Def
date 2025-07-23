"""
 faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor
"""

lista = []
def maior_num():
    for i in range(5):
        num = int(input(f'NUMERO {i+1}: '))
        lista.append(num)
    return f"maior numero da lista {max(lista)}"


print(maior_num())


