from turtle import color
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = 'faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='ricos',
    usecols='A:B',
    nrows=9
)