hi, mi, hf, mf = map(int, input().split())

inicio_minutos = hi * 60 + mi
fim_minutos = hf * 60 + mf

duracao_minutos = fim_minutos - inicio_minutos if fim_minutos > inicio_minutos else fim_minutos - inicio_minutos + 24 * 60

horas = duracao_minutos // 60
minutos = duracao_minutos % 60


print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
