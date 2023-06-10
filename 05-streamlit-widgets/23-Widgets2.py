import pandas as pd
import streamlit as st

df = pd.read_excel(
    io = './Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='Interação',
    usecols='A:C',
    nrows=40,
)
st.subheader('Radio Button')
tipoRelatorio = st.radio(
    "Selecione o tipo de relatório:",
    ('Mensal', 'Semestral', 'Anual'))
st.write('Você selecionou o tipo: ',tipoRelatorio)

st.subheader('Caixa de Seleção')
opcoes = st.selectbox(
    'Selecione a matéria-prima para análise:',
    ('Aço', 'Plástico', 'Borracha', 'Madeira'))
st.write('Você selecionou: ', opcoes)

st.subheader('Seleção múltipla')
multi = st.multiselect(
    'Selecione o banco para consulta: ',
    ['Bradesco', 'Caixa', 'Itaú', 'Banco do Brasil', 'NU Bank'])
st.write(multi)

