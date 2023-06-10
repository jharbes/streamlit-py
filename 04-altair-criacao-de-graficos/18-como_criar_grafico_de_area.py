import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='flow',
    usecols='A:B',
    nrows=15,
)

df # imprime a base de dados



grafico_area=alt.Chart(df).mark_area(
    color='gray',

    # define que haverá uma linha sobre a linha continua do grafico bem como sua cor
    line={'color':'white'}
).encode(

    # :T identifica que se refere a uma serie temporal
    x='Year:T',

    # :Q identifica que se refere a um valor quantitativo
    # setamos o dominio para a escala de 0 a 1400 para ajustar melhor o grafico ao eixo
    y=alt.Y('Value:Q',scale=alt.Scale(domain=(0,1400)))
)


rotulo=grafico_area.mark_text(
    size=14,
    color='red',
    align='center',
    dy=-20
).encode(text='Value')

st.subheader('KPI DE RESULTADOS ANUAIS')

st.altair_chart(grafico_area+rotulo,use_container_width=True)