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


st.subheader('Botão')

# podemos adicionar uma açao ao botao por meio de uma condicional
if st.button('Clique aqui'):
    st.write('Você me clicou')



# funcao para converter o dataframe em arquivo csv
def convert_df(df):
    return df.to_csv().encode('utf-8')


st.subheader('Botão de download')
# botão de download
st.download_button(
    label='Baixar dados em .csv',
    data=convert_df(df),
    file_name='df.csv',
    mime='text/csv'   
)