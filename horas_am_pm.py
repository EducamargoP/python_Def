"""
# 🕐 Desafio: Conversão de horário para formato militar (24 horas)
#
# Objetivo:
# Escreva uma função chamada `timeConversion` que receba uma string representando
# um horário no formato de 12 horas (AM/PM) e converta para o formato de 24 horas.
#
# Regras:
# - "12:00:00AM" deve virar "00:00:00"
# - "12:00:00PM" permanece "12:00:00"
# - "07:05:45PM" deve virar "19:05:45"
#
# Parâmetros:
# - string s: um horário no formato "hh:mm:ssAM" ou "hh:mm:ssPM"
#
# Retorno:
# - Uma string representando o horário no formato de 24 horas
#
# Exemplos:
# Entrada: 07:05:45PM → Saída: 19:05:45
# Entrada: 12:01:00AM → Saída: 00:01:00
# Entrada: 01:15:30AM → Saída: 01:15:30

"""

def time_conversion(s):
    hora = s[:2]
    minuto = s[3:5]
    segundo = s[6:8]
    periodo = s[-2:]

    if periodo == "AM":
        if hora == "12":
            hora = "00"
    else:  # PM
        if hora != "12":
            hora = str(int(hora) + 12)

    return f"{hora}:{minuto}:{segundo}"


if __name__ == '__main__':
    s = input()
    resultado = time_conversion(s)
    print(resultado)



