import pandas as pd
import streamlit as st
import altair as alt


# CRIANDO O DATAFRAME
df=pd.read_excel(
    # path do arquivo excel
    io='../Datasets/system_extraction.xlsx',

    # qual engine vamos utilizar
    engine='openpyxl',

    # nome da aba/planilha do excel
    sheet_name='salesreport',

    # quais colunas vamos usar do dataframe
    usecols='A:J',

    # numero de linhas que vamos importar
    nrows=4400
)


# CRIANDO O SIDEBAR
with st.sidebar:
    st.subheader('MENU - DASHBOARD DE VENDAS')

    # filtro dos vendedores
    filtro_vendedor=st.selectbox(
        'Selecione o Vendedor:',
        options=df['Vendedor'].unique()
    )

    # filtro dos produtos
    filtro_produto=st.selectbox(
        'Selecione o Produto:',
        options=df['Produto vendido'].unique()
    )

    # filtrar os clientes
    filtro_cliente=st.selectbox(
        'Selecione o cliente:',
        options=df['Cliente'].unique()
    )




### 1- Tabela quantidade vendida por produto
tabela_quantidade_produto=df.loc[
    (df['Vendedor']==filtro_vendedor) &
    (df['Cliente']==filtro_cliente)
]

# precisamos resetar o index para podermos usar o grafico após o agrupamento
# faremos tambem a especificacao das colunas a serem somadas, pois caso nao seja feita, o codigo apresentara um erro ao tentar somar a coluna de datas
tabela_quantidade_produto=tabela_quantidade_produto.groupby('Produto vendido')[['Quantidade','Valor Pedido']].sum().reset_index()

tabela_quantidade_produto




### 2- Tabela de Vendas e Margem
tabela_vendas_margem=df.loc[
    (df['Vendedor']==filtro_vendedor) &
    (df['Produto vendido']==filtro_produto) &
    (df['Cliente']==filtro_cliente)
]

tabela_vendas_margem




### 3- Tabela de Vendas por Vendedor
tabela_vendas_vendedor=df.loc[
    (df['Produto vendido']==filtro_produto) &
    (df['Cliente']==filtro_cliente)
]

# precisamos resetar o index para podermos usar o grafico após o agrupamento
# faremos tambem a especificacao das colunas a serem somadas, pois caso nao seja feita, o codigo apresentara um erro ao tentar somar a coluna de datas
tabela_vendas_vendedor=tabela_vendas_vendedor.groupby('Vendedor')[['Quantidade','Valor Pedido']].sum().reset_index()
tabela_vendas_vendedor




### 4- Tabela Vendas por Cliente
tabela_venda_cliente=df.loc[
    (df['Vendedor']==filtro_vendedor) &
    (df['Produto vendido']==filtro_produto)
]

# precisamos resetar o index para podermos usar o grafico após o agrupamento
# faremos tambem a especificacao das colunas a serem somadas, pois caso nao seja feita, o codigo apresentara um erro ao tentar somar a coluna de datas
tabela_venda_cliente=tabela_venda_cliente.groupby('Cliente')[['Quantidade','Valor Pedido']].sum().reset_index()
tabela_venda_cliente




### 5- Vendas Mensais
tabela_vendas_mensais=df.loc[
    (df['Vendedor']==filtro_vendedor) &
    (df['Produto vendido']==filtro_produto) &
    (df['Cliente']==filtro_cliente)
]

# vamos criar colunas específicas para abrigar cada campo da data de forma a facilitar a filtragem
# faremos uma copia da tabela apenas para evitar que o pandas fique propagando uma mensagem de warning sobre possivel copia nao desejada de tabelas
tabela_vendas_mensais = tabela_vendas_mensais.copy()

# Agora, este código não deve gerar um SettingWithCopyWarning
tabela_vendas_mensais['mm'] = tabela_vendas_mensais['Data'].dt.strftime('%m/%Y')
tabela_vendas_mensais







####### PADROES #######
cor_grafico='#FFFFFF'



#### GRAFICOS

# Gráfico 1.0- Quantidade vendida por produto

grafico_quantidade_produto=alt.Chart(tabela_quantidade_produto).mark_bar(
    color=cor_grafico,

    # arredondando as bordas superiores à esquerda das barras do grafico
    cornerRadiusTopLeft=9,

    # arredondando as bordas superiores à direita das barras do grafico
    cornerRadiusTopRight=9,
).encode(
    x='Produto vendido',
    y='Quantidade',
    tooltip=['Produto vendido','Quantidade']
).properties(
    title='QUANTIDADE VENDIDA POR PRODUTO'
).configure_axis(

    # retira a grade do fundo do grafico
    grid=False

    ).configure_view(
    
    # retira as bordas do grafico
    strokeWidth=0
)

st.altair_chart(grafico_quantidade_produto)




# Gráfico 1.1- Valor da venda por produto

grafico_valor_produto=alt.Chart(tabela_quantidade_produto).mark_bar(
    color=cor_grafico,

    # arredondando as bordas superiores à esquerda das barras do grafico
    cornerRadiusTopLeft=9,

    # arredondando as bordas superiores à direita das barras do grafico
    cornerRadiusTopRight=9,
).encode(
    x='Produto vendido',
    y='Quantidade',
    tooltip=['Produto vendido','Valor Pedido']
).properties(
    title='VALOR TOTAL POR PRODUTO'
).configure_axis(

    # retira a grade do fundo do grafico
    grid=False

    ).configure_view(
    
    # retira as bordas do grafico
    strokeWidth=0
)

st.altair_chart(grafico_valor_produto)




# Gráfico 2 - Vendas por Vendedor

grafico_vendas_vendedor=alt.Chart(tabela_vendas_vendedor).mark_arc(
    innerRadius=100,
    outerRadius=150,
).encode(
    theta=alt.Theta(
        field='Valor Pedido',

        # tipo da variavel quantitativa
        type='quantitative',
        stack=True
    ),

    color=alt.Color(
        field='Vendedor',

        # tipo da variavel nominal
        type='nominal',
    ),

    tooltip=['Vendedor','Valor Pedido']
).properties(
    title='VALOR VENDAS POR VENDEDOR',
    height=500,
    width=560
)

rotulo_vendas_vendedor=grafico_vendas_vendedor.mark_text(radius=210, size=14).encode(text='Vendedor')
rotulo_vendas_produto=grafico_vendas_vendedor.mark_text(radius=180, size=12).encode(text='Valor Pedido')

st.altair_chart(grafico_vendas_vendedor+rotulo_vendas_vendedor+rotulo_vendas_produto)




