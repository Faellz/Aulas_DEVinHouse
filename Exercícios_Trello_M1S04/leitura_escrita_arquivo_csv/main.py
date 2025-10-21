'''Crie um script em Python que leia um arquivo CSV contendo informações de vendas (produto, quantidade e valor) 
e gere um novo arquivo CSV com uma coluna adicional chamada “Total”, 
resultado da multiplicação entre quantidade e valor.
Entrega: Arquivo Python (.py) e arquivo CSV gerado.'''

import csv

dados =[["Produto", "Quantidade", "Valor"],
        ["Carne", 5, 19.90],
        ["Arroz", 9, 5.90],
        ["Alface", 2, 2.90] 
        ]
# with open("lista_mercado.csv", "w", newline="", encoding="utf-8") as arquivo:
#     escritor = csv.writer(arquivo)
#     escritor.writerows(dados)

# print("Criou aquivo CSV !!")

novos_dados = []

novos_dados.append(["Produto", "Quantidade", "Valor", "Total"])

for linha in dados[1:]:
    produto, quantidade, valor = linha
    total = quantidade * valor
    novos_dados.append([produto, quantidade, valor, round(total, 2)])

with open("lista_mercado_total.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(novos_dados)
