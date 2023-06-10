import streamlit as st
import pandas as pd
import altair as alt


# GRAFICO DE LINHAS

# Grafico de linhas são muito usados quando temos uma série temporal (uma linha do tempo) e temos a variação de uma determinada medida ao longo do tempo

vendas = pd.DataFrame({
    'Month': ['01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun',
     '07-Jul','08-Ago', '09-Set', '10-Oct', '11-Nov', '12-Dec'],
    'product_A': [28, 55, 43, 91, 81, 53, 19, 87, 52, 85, 101, 77],
    'product_B': [ 93, 68, 79, 84, 81, 97, 109, 99, 125, 115, 120, 88]

})

vendas # imprime o dataframe




st.subheader('GRÁFICO DE LINHAS: PRODUTOS A & B')

grafico_linha_a=alt.Chart(vendas).mark_line().encode(
    # essa forma de definir o eixo X é a forma onde conseguimos parametrizar o campo
    x=alt.X('Month'),

    # y='product_A', # podemos fazer assim porem não poderemos configurar a exibicao desse eixo
    y=alt.Y('product_A')

).properties(
    width=600,
    height=300
)


grafico_linha_b=alt.Chart(vendas).mark_line().encode(
    x=alt.X('Month'),
    y=alt.Y('product_B')
)


rotulo_a=grafico_linha_a.mark_text(
    dy=-15,
    size=14,
    color='white'
).encode(
    text='product_A'
)


rotulo_b=grafico_linha_b.mark_text(
    dy=-15,
    size=14,
    color='yellow'
).encode(
    text='product_B'
)


st.altair_chart(grafico_linha_a+grafico_linha_b+rotulo_a+rotulo_b)