import pandas as pd
import streamlit as st

df = pd.read_excel(
    io = './Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='Interação',
    usecols='A:C',
    nrows=40,
)

st.subheader('Botão')
if st.button("Cliquei aqui"):
    st.write('Você me clicou')

def convert_df(df):
    return df.to_csv().encode('utf-8')
st.subheader('Botão de Download')
st.download_button(
    label="Baixar dados *.csv",
    data=convert_df(df),
    file_name='df.csv',
    mime='text/csv'    
)

st.subheader('Checkbox')
select = st.checkbox('Marque a caixa')
if select ==True:
    st.write('Fui selecionado')