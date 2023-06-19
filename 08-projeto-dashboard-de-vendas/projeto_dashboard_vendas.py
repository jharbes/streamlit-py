import pandas as pd
import streamlit as st
import altair as alt


# CRIANDO O DATAFRAME
df=pd.read_excel(
    # path do arquivo excel
    io='../Datasets/system_extraction.xlsx',

    # qual engine vamos utilizar
    engine='openpyxl',

    # nome da aba/planilha do excel
    sheet_name='salesreport',

    # quais colunas vamos usar do dataframe
    usecols='A:J',

    # numero de linhas que vamos importar
    nrows=4400
)

df