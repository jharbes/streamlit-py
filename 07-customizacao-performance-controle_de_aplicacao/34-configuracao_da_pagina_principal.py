from turtle import color
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='ricos',
    usecols='A:B',
    nrows=10
)


# Cria um sidebar para filtrar os bilionarios no df e gráfico
st.sidebar.header('Filtre aqui:')
bilionarios=st.sidebar.multiselect(
    'Selecione os bilionários:',
    options=df['Nome'].unique(),
    default=df['Nome'].unique()
)

# Cria uma nova versão do df conforme filtros aplicados
df_filtrado=df.query(
    'Nome == @bilionarios'
)



graf_pizza = alt.Chart(df_filtrado).mark_arc(
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


st.header('Gráfico de Pizza/Arco')
st.subheader('Os mais ricos do mundo')
st.altair_chart(graf_pizza+rotuloNome+rotuloValor)