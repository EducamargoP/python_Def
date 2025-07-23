""""
- crie um programa que tenha uma função que receba um parametro inteiro e devolva o seu dobro
"""

def dobro_num():
    soma = num * 2
    return f"o dobro de {num} e {soma}"

num = int(input("NUMERO:"))
print(dobro_num())
