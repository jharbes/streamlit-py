import pandas as pd
import streamlit as st

df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='Interação',
    usecols='A:C',
    nrows=40,
)

df # imprime o dataframe



### RADIO BUTTON
st.subheader('Radio Button')

tipo_relatorio=st.radio(
    'Selecione o tipo de relatório:',
    ('Mensal','Semestral','Anual')
)

st.write('Você selecionou o tipo: ',tipo_relatorio)



### CAIXA DE SELECAO (DROP BOX)
st.subheader('Caixa de seleção')

opcoes=st.selectbox(
    'Selecione a matéria-prima para análise:',
    ('Aço','Plástico','Borracha','Madeira')
)

st.write('Você selecionou: ',opcoes)



### SELECAO MULTIPLA (permite escolher várias opções)
st.subheader('Seleção Múltipla')

selecao_multipla=st.multiselect(
    'Selecione o banco para consulta: ',
    ['Bradesco','Caixa','Itáu','Banco do Brasil','NuBank']
)

st.write(selecao_multipla) # mostrara as opções em forma de lista

st.write(selecao_multipla[0]) # nesse caso mostrará apenas a opção cujo indice está com o valor ao lado em colchetes (lista)