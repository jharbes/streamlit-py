import pandas as pd
import streamlit as st
import datetime

st.subheader('Slider')
parcelas = st.slider(
    'Com quantas parcelas deseja simular?', 0, 60,30)
st.write('Você selecionou', parcelas, 'Parcelas')

intervalo = st.slider(
    'Qual o intervalo desejado?',
    0.0, 100.0, (25.0, 75.0))
st.write('Intervalo:', intervalo)


st.subheader('Datas')
d = st.date_input(
    'Selecione a data: ',
    datetime.date(2022,10,1)
)
st.write('A data selecionada foi: ',d)


