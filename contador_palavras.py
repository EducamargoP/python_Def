"""
Crie um programa que receba uma frase do usuário e conte quantas palavras existem nela.
A saída deve informar o total de palavras encontradas.
"""

texto = str(input("DIGA UMA FRASE: ")).split()

lista = texto
print(lista)
print(f'a frase tem {len(lista)} palavras')
