import pandas as pd

df = pd.read_excel('./system_extraction.xlsx')

print(df) # imprime o dataframe


print(df.head(5)) # imprime apenas as cinco primeiro linhas para dar nocao de como ele é


df = df.drop(columns=['Região', 'Preço']) # deletando as colunas 'Região' e 'Preço'

print(df)



print(df.loc[df['Vendedor'] == 'Paulo']) # loc (localize) para filtrar a tabela apenas com o 'Vendedor' que seja 'Paulo"


print(df.loc[df['Vendedor'] == 'Paulo', ['Valor Pedido']]) # vai filtar o Vendedor Paulo porém a tabela só retornará a coluna 'Valor Pedido'



print(df.groupby(['Produto vendido']).sum()) # agrupa pelo produto vendido e soma as colunas

print(df.groupby(['Produto vendido']).mean()) # agrupa pelo produto vendido e mostra a media das colunas



print(len(df)) # retorna o numero de linhas do dataframe



df['marg_porc'] = 100*df['Margem Lucro'] / df['Valor Pedido'] # criamos a coluna 'marg_porc' que é a margem percentual adicionando ela ao dataframe

print(df) # imprimimos o dataframe



print(df['Nº pedido'].where(df['marg_porc'] > 20, "menor que 20")) # filtramos a coluna numero de pedido onde a margem percentual de lucro é maior que 20, nos casos onde não for maior que 20 ela vai imprimir 'menor que 20'



print(df['Cliente'].unique()) # imprime a coluna cliente sem repeticoes

print(df['Cliente'].nunique()) # imprime o numero de clientes sem contar as repeticoes




print(df.nunique()) # retorna os valores unicos de cada coluna da tabela



print(df.sort_values(by='Nº pedido', ascending=True)) # classifica o dataframe em ordem crescente de numero de pedido
