import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = '../Datasets/normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87,
)

df # imprimir o dataframe


# histograma nada mais é do que um grafico de barras
histograma=alt.Chart(df).mark_bar().encode(
    x=alt.X('x'),
    y='count'
)


st.subheader('HISTOGRAMA - NOTAS DE 1000 ALUNOS')

st.altair_chart(histograma,use_container_width=True)




# faremos alteracao agora no histograma para em vez de aparecer cada um das notas para aparecer por 'faixa de notas', no caso com step=10 as notas ficarao divididas me faixas de 10 em 10 notas
histograma=alt.Chart(df).mark_bar().encode(
    x=alt.X('x',bin=alt.Bin(step=10)),

    # teremos que colocar no eixo y o somatorio para que o grafico fique mostre o total, caso contrario ele mostrará varias faixas empilhadas (tambem está ok)
    y='count'
    # y='sum(count)'
)


st.subheader('HISTOGRAMA2 - FAIXAS DE 10 NOTAS - NOTAS DE 1000 ALUNOS')

st.altair_chart(histograma,use_container_width=True)