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

histograma=alt.Chart(df).mark_bar().encode(
    x=alt.X('x',bin=alt.Bin(step=5)),

    y='count'
    # y='sum(count)'
)

st.subheader('HISTOGRAMA2 - FAIXAS DE 10 NOTAS - NOTAS DE 1000 ALUNOS')

st.altair_chart(histograma,use_container_width=True)

df