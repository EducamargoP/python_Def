"""
Objetivos do Código:
Criar uma função que receba a idade de uma pessoa como parâmetro.

Retornar se a pessoa é menor de idade, adulto ou idoso, com base nos seguintes critérios:

Menor de idade: idade < 18

Adulto: idade entre 18 e 60

Idoso: idade > 60
"""


def verificar_idade(idade):

    if idade > 60:
        return "Você tem uma idade considerada idoso"
    elif idade < 18:
        return "Você e menor de idade!"
    elif idade >= 18:
        return "Você é adulto!"
idade = int(input('Diga sua idade: '))
print(verificar_idade(idade))
