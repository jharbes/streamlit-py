from turtle import color
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = 'faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='ricos',
    usecols='A:B',
    nrows=9
)

st.subheader('GRÁFICO PIZZA - MAIS RICOS DO MUNDO')

graf_pizza = alt.Chart(df).mark_arc(
    innerRadius=0,
    outerRadius=150
).encode(
    theta = alt.Theta(field='Fortuna', type='quantitative', stack=True),
    color=alt.Color(
        field='Nome', 
        type='nominal',
        #legend=None
    ),
    tooltip = ['Nome', 'Fortuna']
).properties(width=700, height=450)

rotuloNome = graf_pizza.mark_text(radius=200, size=14).encode(text='Nome')
rotuloValor = graf_pizza.mark_text(radius=165, size=14).encode(text='Fortuna')
st.altair_chart(graf_pizza+rotuloNome+rotuloValor)