def ler_consumos_semanais(dias: int = 7):
    consumos = []
    print("===== Monitoramento de Consumo de Água =====")
    for i in range(1, dias + 1):
        while True:
            try:
                entrada = input(f"Informe o consumo de água (em litros) para o Dia {i}: ")

                entrada = entrada.replace(",", ".")
                valor = float(entrada)
                if valor < 0:
                    print("Valor não pode ser negativo. Tente denovo.")
                    continue
                consumos.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    return consumos
