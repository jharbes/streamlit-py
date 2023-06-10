import pandas as pd
import streamlit as st

df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='Interação',
    usecols='A:C',
    nrows=40,
)

