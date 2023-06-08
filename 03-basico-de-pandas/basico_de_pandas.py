import pandas as pd

df = pd.read_excel('./system_extraction.xlsx')

df # imprime o dataframe no jupyter ou google colab


df.head(5) # imprime apenas as cinco primeiro linhas para dar nocao de como ele é


df = df.drop(columns=['Região', 'Preço']) # deletando as colunas 'Região' e 'Preço'

df



df.loc[df['Vendedor'] == 'Paulo'] # loc (localize) para filtrar a tabela apenas com o 'Vendedor' que seja 'Paulo"


df.loc[df['Vendedor'] == 'Paulo', ['Valor Pedido']] # vai filtar o Vendedor Paulo porém a tabela só retornará a coluna 'Valor Pedido'


