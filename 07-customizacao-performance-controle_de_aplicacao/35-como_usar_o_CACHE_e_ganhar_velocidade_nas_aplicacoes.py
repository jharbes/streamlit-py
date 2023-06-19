import pandas as pd
import streamlit as st

df=pd.read_excel(
    io='../Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='cache_teste',
    usecols='A:E',
    nrows=100000,
)


# SIDEBAR
st.sidebar.header('MENU')
selecao_cliente=st.sidebar.multiselect(
    'Selecione o cliente',
    options=df['Cliente'].unique(),
    default=df['Cliente'].unique()
)


