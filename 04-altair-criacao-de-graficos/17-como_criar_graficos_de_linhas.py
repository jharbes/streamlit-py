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

grafico_linha_A=alt.Chart(vendas).mark_line(
    # define a cor da linha do grafico
    color='red',
    
    # define que existe um ponto em cada local dos pontos enumerados do product_A e sua cor, color define sua cor, size o seu tamanho, filled se ele estará preenchido ou nao e fill qual cor de preenchimento
    point=alt.OverlayMarkDef(color='red',size=70,filled=False, fill='black'),

).encode(
    # essa forma de definir o eixo X é a forma onde conseguimos parametrizar o campo
    x=alt.X('Month'),

    # y='product_A', # podemos fazer assim porem não poderemos configurar a exibicao desse eixo
    # retiramos as linhas de grid do grafico com a expressao axis=alt.Axis(grid=False) (linhas pontilhadas como no excel)
    # com scale alteramos a escala do grafico para que tenha seu dominio entre 0 e 160 de modo que ele fique completamente inserido ao eixo y
    y=alt.Y('product_A',axis=alt.Axis(grid=False),scale=alt.Scale(domain=(0,160))),

    # o tooltip mostrará os valores daquele ponto quando passarmos o mouse por cima (hover) em uma janela a parte ajudando tambem a visualizacao dos valores
    tooltip=['Month','product_A','product_B']

).properties(
    width=600,
    height=300,

    # adiciona um título ao gráfico
    title='VENDAS MENSAIS DOS PRODUTOS A & B'
)


grafico_linha_B=alt.Chart(vendas).mark_line(
    # define a cor da linha do grafico
    color='yellow',
    
    # define que existe um ponto em cada local dos pontos enumerados do product_A e sua cor
    point=alt.OverlayMarkDef(color='yellow',size=70,filled=False, fill='black'),
).encode(
    x=alt.X('Month'),
    y=alt.Y('product_B'),

    # o tooltip mostrará os valores daquele ponto quando passarmos o mouse por cima (hover) em uma janela a parte ajudando tambem a visualizacao dos valores
    tooltip=['Month','product_A','product_B']
)


rotulo_A=grafico_linha_A.mark_text(
    dy=-15,
    size=14,
    color='white'
).encode(
    text='product_A'
)


rotulo_B=grafico_linha_B.mark_text(
    dy=-15,
    size=14,
    color='gray'
).encode(
    text='product_B'
)


st.altair_chart(grafico_linha_A+grafico_linha_B+rotulo_A+rotulo_B)