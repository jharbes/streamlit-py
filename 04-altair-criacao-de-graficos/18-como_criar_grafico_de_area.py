import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = 'faturamento.xlsx',
    engine='openpyxl',
    sheet_name='flow',
    usecols='A:B',
    nrows=15,
)