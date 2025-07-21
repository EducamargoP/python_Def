"""
Crie um programa que funcione como uma lista de tarefas para o usuário.
O sistema deve permitir adicionar novos itens à lista, remover itens existentes
 e visualizar todas as tarefas cadastradas.
"""

lista = []

while True:
    print("#" * 10)
    print('---- MENU ----')
    print("0 PARA ENCERRAR!")
    print("1 ADICIONAR TAREFA")
    print("2 REMOVER TAREFA")
    print("3 VER LISTA TAREFA")

    print("#" * 10)
    contador = input("QUAL OPÇÃO DESEJA: ")
    if contador == "1":
        tarefa = input("DIGA A TAREFA: ")
        lista.append(tarefa)
    elif contador == "2":
        tarefa = int(input("CONTE E DIGA O NUMERO DA TAREFA QUE DESEJA REMOVER; "))
        lista.pop(tarefa-1)
    elif contador == "3":
         print(lista)
    elif contador == "0":
        break

