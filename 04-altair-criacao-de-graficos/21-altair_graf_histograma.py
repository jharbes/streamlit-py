import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = './Datasets/normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87,
)
Histograma = alt.Chart(df).mark_bar().encode(
    x = alt.X('x', bin=alt.Bin(step=5)),
    y='sum(count)'
)
st.subheader('HISTOGRAMA - NOTAS DE 1000 ALUNOS')
st.altair_chart(Histograma,use_container_width=True)