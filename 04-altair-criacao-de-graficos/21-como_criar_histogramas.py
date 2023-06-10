import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_excel(
    io = '../Datasets/normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87,
)

df # imprimir o dataframe

