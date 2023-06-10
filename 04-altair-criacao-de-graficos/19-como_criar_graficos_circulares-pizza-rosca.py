from turtle import color
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='ricos',
    usecols='A:B',
    nrows=9
)


df # imprime o dataframe


st.subheader('GRÁFICO DE PIZZA - MAIS RICOS DO MUNDO')

grafico_pizza=alt.Chart(df).mark_arc(

    # raio interno, se aumentarmos o innerRadius teremos um espaço vazio no meio, ou seja, passará a ser um gráfico de rosca
    innerRadius=0, 

    # raio externo
    outerRadius=150
     
).encode(

    # theta é necessário para os gráficos de pizza
    # escolhemos o que será demonstrado, o tipo de dado e se queremos empilhamento (stack)
    theta=alt.Theta(field='Fortuna',type='quantitative',stack=True),

    # a cor será definida pelo nome da pessoa, cada uma terá uma cor
    # legend=None irá retirar a legenda das cores
    color=alt.Color(
        field='Nome',
        type='nominal',
        legend=None
    ),

    tooltip=['Nome','Fortuna']
).properties(
    width=750,
    height=500
)


# radius será a distancia que ficara o rotulo do centro da pizza
rotulo_nome=grafico_pizza.mark_text(radius=210,size=14).encode(
    text='Nome'
)

rotulo_valor=grafico_pizza.mark_text(radius=165,size=14).encode(
    text='Fortuna',
)


st.altair_chart(grafico_pizza+rotulo_nome+rotulo_valor)