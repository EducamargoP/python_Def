"""
Crie uma calculadora simples que receba dois valores numéricos do usuário.
Em seguida, o programa deve permitir escolher o tipo de operação matemática a ser realizada (adição, subtração, multiplicação ou divisão), e exibir o resultado.
"""



while True:
    num1 = int(input('diga primeiro numero:'))
    num2 = int(input('diga segundo numero:'))
    print("#" * 10)
    print("1 ADIÇÃO")
    print("2 SUBTRAÇÃO")
    print("3 MUTIPLICAÇÃO")
    print("4 DIVISÃO")
    print('5 ENCERRA')
    print("#" * 10)

    escolha = int(input("QUAL DESEJA: "))
    print("#" * 10)
    if  escolha == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif escolha == 2:
        soma = num1 - num2
        print(f'{num1} - {num2} = {soma}')
    elif escolha == 3:
        soma = num1 * num2
        print(f'{num1} x {num2} = {soma}')
    elif escolha == 4:
        soma = num1 / num2
        print(f'{num1} % {num2} = {soma}')

    elif escolha ==5:
        break
print('OBRIGADO VOLTE SEMPRE')