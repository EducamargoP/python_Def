""""
  faça um programa que tenha uma função que receba uma data no formato string exemplo "01/011/2024"
 e imprima ela por extenso como 1 de janeiro de 2024"
"""

def meses_valor():
    d = input('DATA (DD/MM/YYYY): ')
    valor= d.split("/")
    dia = int(valor[0])
    mes = int(valor[1])
    ano = int(valor[2])
    if mes == 1:
        return "JANEIRO"
    elif mes == 2:
        return F"{dia} FEVEREIRO {ano}"
    elif mes == 3:
        return f"{dia} MARÇO {ano}"
    elif mes == 4:
        return f"{dia} ABRIL {ano}"
    elif mes == 5:
        return f"{dia} MAIO {ano}"
    elif mes == 6:
        return f"{dia} JUNHO {ano}"
    elif mes == 7:
        return f"{dia} JULHO {ano}"
    elif mes == 8:
        return f"{dia} AGOSTO {ano}"
    elif mes == 9:
        return f"{dia} SETEMBRO {ano}"
    elif mes == 10:
        return f"{dia} OUTUBRO {ano}"
    elif mes == 11:
        return f"{dia} NOVEMBRO {ano}"
    elif mes == 12:
        return f"{dia} DEZEMBRO {ano}"
    else:
        "MES DESCONHECIDO"


    return f"essa foi a data passada {d}"
print(meses_valor())



