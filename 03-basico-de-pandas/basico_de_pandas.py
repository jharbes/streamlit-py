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



