from turtle import color
import altair as alt
from numpy import size
import pandas as pd
import streamlit as st

fonte = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

fonte # imprime o dataframe

grafico_barras=alt.Chart(fonte).mark_bar().encode(
    x='a',
    y='b',
    color='a', # nesse caso setamos para que cada rotulo tenha uma cor diferente
    tooltip=['a','b'] # essa opcao fará com que ao passar por cima apareça uma tooltip (ajuda no gráfico)
)

rotulo_barra=grafico_barras.mark_text(
    dy=-8, # posicao do rótulo em relaçao a barra
    size=17 # tamanho do texto do rótulo(acima das barras)
).encode(
    text='b' # o que vai aparecer no rótulo (acima das barras, valor de 'b')
)

st.subheader('Abaixo a representação do dataset de cima com representação de BARRAS:')

# use_container_width= True faz com que ele use toda a largura do container para esse gráfico
# o +rotulo adiciona o rótulo escolhido criado acima (numeros acima das barras para facilitar saber o valor de cada barra ao visualizar o grafico)
st.altair_chart(grafico_barras+rotulo_barra, use_container_width=True)




# CRIANDO GRAFICO DE AREA

grafico_area=alt.Chart(fonte).mark_area(
    color='lightblue',
    interpolate='step-after',
    line=True # coloca uma linha em volta do grafico para melhor apresentacao
).encode(
    x='a',
    y='b',
    tooltip=['a','b']
)

rotulo_area=grafico_area.mark_text(
    dy=-8, # posicao do rótulo em relaçao a barra
    dx=30,
    color='white',
    size=17 # tamanho do texto do rótulo(acima das barras)
).encode(
    text='b' # o que vai aparecer no rótulo (acima das barras, valor de 'b')
)

st.subheader('Gráfico de ÁREA')

st.altair_chart(grafico_area+rotulo_area,use_container_width=True)