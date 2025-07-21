""""
✅ Objetivos do Código:
Criar uma função usando a palavra-chave def

Receber três notas como parâmetros

Calcular a média das notas

Usar estrutura condicional if, elif, else para verificar a situação do aluno

Retornar uma string indicando se o aluno foi "Aprovado", "Recuperação" ou "Reprovado"

Utilizar print() para exibir o resultado
"""


def aprovado_reprovado (nota1, nota2, nota3):

    soma = (nota1 + nota2 + nota3) / 3
    if soma < 4:
        return "REPROVADO!"
    elif soma == 5:
        return "RECUPERAÇÃO"
    elif soma >= 6:
        return "APROVADO"
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
print(aprovado_reprovado(nota1, nota2, nota3))
