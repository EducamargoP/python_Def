"""
Regra principal:
A cada novo jogo, compare a pontuação com os recordes atuais de maior e menor pontuação:

Se a pontuação for maior que o recorde atual de pontos máximos, incrementa o contador de recordes máximos.

Se for menor que o recorde atual de pontos mínimos, incrementa o contador de recordes mínimos.

Depois de cada comparação, atualize o recorde quando ele for quebrado
"""

def breakingRecords(scores):
    max_record = min_record = scores[0]
    max_breaks = min_breaks = 0

    for score in scores[1:]:
        if score > max_record:
            max_record = score
            max_breaks += 1
        elif score < min_record:
            min_record = score
            min_breaks += 1

    return [max_breaks, min_breaks]


n = int(input())
scores = list(map(int, input().split()))
resultado = breakingRecords(scores)
print(*resultado)



