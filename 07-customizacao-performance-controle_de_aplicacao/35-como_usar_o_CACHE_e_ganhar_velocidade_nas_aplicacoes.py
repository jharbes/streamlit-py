import pandas as pd
import streamlit as st


# O streamlit vai armazenar no cache da maquina todo o dataset, ou seja, vai carregar todo o dataset na primeira vez e todos os outros filtros serao muito rapidos
@st.cache_data
def busca_df():
    df=pd.read_excel(
        io='../Datasets/faturamento.xlsx',
        engine='openpyxl',
        sheet_name='cache_teste',
        usecols='A:E',
        nrows=100000,
    )
    return df


df=busca_df()


# SIDEBAR
st.sidebar.header('MENU')
selecao_cliente=st.sidebar.multiselect(
    'Selecione o cliente',
    options=df['Cliente'].unique(),
    default=df['Cliente'].unique()
)


# Cria um novo df conforme filtro e cliente
df_filtro_cliente=df.query(
    'Cliente == @selecao_cliente'
)


# Adiciona ao side bar a selecao da coluna a exibir
selecao_colunas=st.sidebar.multiselect(
    'Selecione a coluna a exibir',
    options=list(df_filtro_cliente),default=list(df_filtro_cliente)
)

df_printado=df_filtro_cliente.filter(items=selecao_colunas)



st.header('Como usar o *CACHE* no **Streamlit** ')
df_printado