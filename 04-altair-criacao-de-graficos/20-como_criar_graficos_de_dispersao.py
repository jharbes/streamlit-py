import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv('../Datasets/vega_car.csv')

df # imprimindo o dataframe


# esse dataframe mostra o consumo de gasolina de alguns veículos conforme o numero de cavalos do motor
# vamos ver a relacao entre o consumo de combustivel e quantos cavalos tem o motor e verificar se conseguimos criar um grafico de dispersao que mostre a variacao dessas duas variaveis.


grafico_dispersao=alt.Chart(df).mark_point().encode(
    
    # :Q medida quantitativa
    x='Horsepower:Q',

    y='Miles_per_Gallon',

    # alterando o valor da cor de acordo com o local de origem do carro (europe, usa, japan)
    color=alt.Color('Origin:N')
)


st.subheader('GRÁFICO DE DISPERSÃO: CONSUMO POR NUMERO DE HORSEPOWER')

st.altair_chart(grafico_dispersao,use_container_width=True)