import streamlit as st
import altair as alt
import pandas as pd

source = pd.read_csv('../Datasets/vega_car.csv')

source # imprimindo o dataframe


# esse dataframe mostra o consumo de gasolina de alguns veículos conforme o numero de cavalos do motor
# vamos ver a relacao entre o consumo de combustivel e quantos cavalos tem o motor e verificar se conseguimos criar um grafico de dispersao que mostre a variacao dessas duas variaveis.


