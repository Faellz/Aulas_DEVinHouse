import coleta,calculo,relatorio

consumos = coleta.ler_consumos_semanais()
total = calculo.calcular_total(consumos)    
media = calculo.calcular_media(consumos)
avaliacao = calculo.avaliar_consumo(media)
relatorio.gerar_relatorio(total, media, avaliacao)
