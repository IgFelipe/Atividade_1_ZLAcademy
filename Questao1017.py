
def calcular_consumo_combustivel(tempo_viagem, velocidade_media):
   
    eficiencia = 12
    distancia = tempo_viagem * velocidade_media
    consumo_combustivel = distancia / eficiencia

    return consumo_combustivel

tempo_viagem = int(input())
velocidade_media = int(input())

resultado = calcular_consumo_combustivel(tempo_viagem, velocidade_media)

print(f"{resultado:.3f}")