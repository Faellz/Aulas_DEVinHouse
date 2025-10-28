'''Importe os arquivos clientes.csv, pedidos.csv e produtos.csv usando Pandas. Explore os dados para entender sua estrutura.'''
import pandas as pd

#Lendo os arquivos com read_csv 
df_clientes = pd.read_csv('clientes.csv')
df_pedidos = pd.read_csv('pedidos.csv')
df_produtos = pd.read_csv('produtos.csv')
print(df_produtos.head())

# Verificando tipos e nulos com .info() e isnull.sum()
df_produtos.info()
df_produtos.isnull().sum()

# Obtendo estatísticas com o describe()
df_produtos.describe() 

'''Aplique filtros para extrair informações específicas dos DataFrames.'''

# Selecionar clientes com idade > 30
clientes_maior_30 = df_clientes[df_clientes['idade'] > 30]
print('\nAqui está a lista de clientes com mais de 30 anos:\n', clientes_maior_30)

# Filtrar pedidos com valor > R$500
pedidos_maior_500 = df_pedidos[df_pedidos['valor_total'] > 500]
print('\nPedidos com valor total maior que R$500:\n',pedidos_maior_500)

# Selecionar produtos da categoria "Eletrônicos"
eletros = df_produtos[df_produtos['categoria'].str.contains('Eletrônicos')]
print('\nAqui estão os itens com categoria eletrônicos:\n',eletros)

# Usar .loc[] e iloc[] para seleções
print('\n', df_produtos.loc[5]) # Linha com índice 5 / Por rotulos

print('\n', df_produtos.iloc[0]) # Primeira linha de produtos / Pelos índices
print('\n', df_produtos.iloc[0:5]) # Primeiras 5 linhas  / Pelos índices


'''Realize operações para cruzar e resumir os dados.'''
# Juntar clientes e pedidos (merge)
df_merged = pd.merge(df_clientes, df_pedidos, on='id_cliente')
print('\nMerge de pedidos.csv + clientes.csv usando a coluna "id_cliente"\n',df_merged)

# Agrupar pedidos por cliente e somar valores (groupby)
total_por_cliente = df_merged.groupby('nome')['valor_total'].sum().reset_index()
print('\nValor de gastos totais por cliente:\n',total_por_cliente)

# Criar tabela dinâmica com categorias e média de preços (pivot_table)
media_produtos = df_produtos.pivot_table(values='preco', index='categoria', aggfunc='mean')
media_produtos

# Verificar duplicatas e limpar dados se necessário
duplicatas_1 = df_merged[df_merged.duplicated()]
print('\n',duplicatas_1)
duplicatas_2 = df_produtos[df_produtos.duplicated()]
print('\n',duplicatas_2)

print('\nTotal de valores ausentes nas colunas de df_merged: \n',df_merged.isnull().sum())
print('\nTotal de valores ausentes nas colunas de df_produtos: \n',df_produtos.isnull().sum())


'''Utilize NumPy para cálculos e simulações com arrays'''

#Importar NumPy como np
import numpy as np

#Criar array com valores dos pedidos
array_valor_pedidos = np.array(df_pedidos['valor_total'])
print('\nArray com o valores dos pedidos:',array_valor_pedidos)

#Calcular média, soma e desvio padrão
print('\nMédia:', np.mean(array_valor_pedidos))
print('\nSoma:', np.sum(array_valor_pedidos))
print('\nDesvio:', np.std(array_valor_pedidos))

#Aplicar desconto de 10% com broadcasting
array_com_desconto10 = array_valor_pedidos * 0.90
print('\nDesconto de 10%:',array_com_desconto10)

#Verificar tipos e dimensões com .dtype() e .shape()
print('\nTipos:', array_valor_pedidos.dtype)
print('\nDimensão:', array_valor_pedidos.shape)


'''Produza um resumo com os principais insights da análise.'''

# Identificar o cliente que mais gastou
maior_valor = df_pedidos['valor_total'].max()
maior_index = df_pedidos['valor_total'].idxmax()
cliente_rico = df_clientes.loc[maior_index, 'nome']
print(f'\nO cliente que mais gastou é {cliente_rico} com R$ {maior_valor:.2f}')

# Calcular ticket médio por categoria
ticket_medio_categoria = df_produtos.groupby('categoria')['preco'].mean().reset_index()
ticket_medio_categoria.rename(columns={'preco': 'ticket_medio'}, inplace=True)
print('\nTicket médio por categoria:\n', ticket_medio_categoria)

# Verificar cidade com maior número de clientes
clientes_por_cidade = df_clientes['cidade'].value_counts().reset_index()
clientes_por_cidade.columns = ['cidade', 'qtd_clientes']
cidade_top = clientes_por_cidade.iloc[0]
print(f'\nA cidade com maior número de clientes é {cidade_top["cidade"]} com {cidade_top["qtd_clientes"]} clientes.')
print('\nRanking de cidades:\n', clientes_por_cidade)

# Criar visualizações (opcional)
...
