import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import openpyxl

# CONFIGURAÇÕES DE PÁGINA

st.set_page_config(
    page_title='DASHBOARD DE VENDAS - by J.HARBES',
    page_icon='📈',

    # inicia o layout em wide (ocupa a tela toda)
    layout='wide',

    # sidebar inicia aberto
    initial_sidebar_state='expanded',

    menu_items={
        'Get Help':'https://github.com/jharbes',
        'Report a bug':'https://github.com/jharbes',
        'About':'Dashboard desenvolvido por J.Harbes'
    }
)


# CRIANDO O DATAFRAME
df=pd.read_excel(
    # path do arquivo excel
    io='./Datasets/system_extraction.xlsx',

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
    # logo_sidebar=Image.open('../Mídia/logo vizion.png')
    # st.image(logo_sidebar, width=300)

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

# tabela_quantidade_produto




### 2- Tabela de Vendas e Margem
tabela_vendas_margem=df.loc[
    (df['Vendedor']==filtro_vendedor) &
    (df['Produto vendido']==filtro_produto) &
    (df['Cliente']==filtro_cliente)
]

# tabela_vendas_margem




### 3- Tabela de Vendas por Vendedor
tabela_vendas_vendedor=df.loc[
    (df['Produto vendido']==filtro_produto) &
    (df['Cliente']==filtro_cliente)
]

# precisamos resetar o index para podermos usar o grafico após o agrupamento
# faremos tambem a especificacao das colunas a serem somadas, pois caso nao seja feita, o codigo apresentara um erro ao tentar somar a coluna de datas
tabela_vendas_vendedor=tabela_vendas_vendedor.groupby('Vendedor')[['Quantidade','Valor Pedido']].sum().reset_index()

# tabela_vendas_vendedor




### 4- Tabela Vendas por Cliente
tabela_venda_cliente=df.loc[
    (df['Vendedor']==filtro_vendedor) &
    (df['Produto vendido']==filtro_produto)
]

# precisamos resetar o index para podermos usar o grafico após o agrupamento
# faremos tambem a especificacao das colunas a serem somadas, pois caso nao seja feita, o codigo apresentara um erro ao tentar somar a coluna de datas
tabela_venda_cliente=tabela_venda_cliente.groupby('Cliente')[['Quantidade','Valor Pedido']].sum().reset_index()

# tabela_venda_cliente




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

# tabela_vendas_mensais






####### PADROES #######
cor_grafico='#9dd1f1'
altura_grafico=250



#### GRAFICOS

### Gráfico 1.0- Quantidade vendida por produto

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
    height=altura_grafico,
    title='QUANTIDADE VENDIDA POR PRODUTO'
).configure_axis(

    # retira a grade do fundo do grafico
    grid=False

    ).configure_view(
    
    # retira as bordas do grafico
    strokeWidth=0
)






### Gráfico 1.1- Valor da venda por produto

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
    height=altura_grafico,
    title='VALOR TOTAL POR PRODUTO'
).configure_axis(

    # retira a grade do fundo do grafico
    grid=False

    ).configure_view(
    
    # retira as bordas do grafico
    strokeWidth=0
)






### Gráfico 2 - Vendas por Vendedor

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
        legend=None
    ),

    tooltip=['Vendedor','Valor Pedido']
).properties(
    title='VALOR VENDAS POR VENDEDOR',
    height=600,
    width=560
)

rotulo_vendas_vendedor=grafico_vendas_vendedor.mark_text(radius=210, size=14).encode(text='Vendedor')
rotulo_vendas_produto=grafico_vendas_vendedor.mark_text(radius=180, size=12).encode(text='Valor Pedido')






### Gráfico 3- Vendas por Cliente

grafico_vendas_cliente=alt.Chart(tabela_venda_cliente).mark_bar(
    color=cor_grafico,

    # arredondando as bordas superiores à esquerda das barras do grafico
    cornerRadiusTopLeft=9,

    # arredondando as bordas superiores à direita das barras do grafico
    cornerRadiusTopRight=9,
).encode(
    x='Cliente',
    y='Valor Pedido',
    tooltip=['Cliente','Valor Pedido']
).properties(
    title='VENDAS POR CLIENTE',
    height=altura_grafico
).configure_axis(

    # retira a grade do fundo do grafico
    grid=False

    ).configure_view(
    
    # retira as bordas do grafico
    strokeWidth=0
)






### Gráfico 4- Vendas Mensais

grafico_vendas_mensais=alt.Chart(tabela_vendas_mensais).mark_line(
    color=cor_grafico,
).encode(
    # :T - tipo temporal
    alt.X('monthdate(Data):T'),

    # :Q - tipo quantitativo
    y='Valor Pedido:Q'
).properties(
    title='VENDAS MENSAIS',
    height=altura_grafico
).configure_view(
    strokeWidth=0
)





#### PÁGINA PRINCIPAL

total_vendas=round(tabela_vendas_margem['Valor Pedido'].sum(),2)
total_margem=round(tabela_vendas_margem['Margem Lucro'].sum(),2)
percentual_margem=int(100*total_margem/total_vendas)

st.header(':bar_chart: DASHBOARD DE VENDAS - by J.HARBES')


# vamos criar agora as variaveis que serão as colunas que darão espaçamento entre um gráfico e outro
destaque1,destaque2,destaque3,destaque4=st.columns([1,1,1,2.5])



with destaque1:
    # os dois asteristicos entre a frase é pra deixá-lo em negrito
    st.write('**VENDAS TOTAIS:**')
    st.info(f'R$ {total_vendas}')


with destaque2:
    st.write('**MARGEM TOTAL:**')
    st.info(f'R$ {total_margem}')


with destaque3:
    st.write('**MARGEM EM %:**')
    st.info(f'{percentual_margem}')


# faz uma linha dividindo as partes da pagina
st.markdown('---')



# Colunas dos Gráficos
coluna1,coluna2,coluna3=st.columns([1,1,1])


with coluna1:

    # use_container_width=True faz com que o grafico utilize toda a largura do container onde ele está contido
    st.altair_chart(grafico_vendas_cliente,use_container_width=True)
    st.altair_chart(grafico_vendas_mensais,use_container_width=True)


with coluna2:
    st.altair_chart(grafico_quantidade_produto,use_container_width=True)
    st.altair_chart(grafico_valor_produto,use_container_width=True)


with coluna3:
    st.altair_chart(grafico_vendas_vendedor+rotulo_vendas_vendedor+rotulo_vendas_produto,use_container_width=True)


st.markdown('---')