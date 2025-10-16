def calcular_total(consumos):
    if len(consumos) == 7:
        total_consumido = sum(consumos)
        return total_consumido
    else:
        raise ValueError("A lista deve conter exatamente 7 valores.")

def calcular_media(consumos):
    total = calcular_total(consumos)
    return total / len(consumos)

def avaliar_consumo(media):
    if media<150:
        return "Consumo abaixo da média sustentável"
    elif media>=150 and media<= 200:
        return "Consumo dentro da média sustentável"
    else:
        return "Consumo acima da média sustentável"
