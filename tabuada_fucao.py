""""
Exercício Função: Tabuada
Escreva uma função chamada tabuada() que:

Recebe um número inteiro como parâmetro.

Imprime a tabuada desse número de 1 a 10.

Retorna uma lista com os resultados da tabuada.
"""

def tabuada(n):
    lista = []
    for i in range(0, 11):
        resultado = n *  i
        lista.append(f" {n} x {i} = {resultado}")
    return (lista)

num = int(input("NUMERO PARA TABUADA: "))
print(tabuada(num))

