import pandas as pd
import streamlit as st
import datetime


### SLIDER
st.subheader('Slider')

parcelas = st.slider(
    'Com quantas parcelas deseja simular?', 0, 60,30)
st.write('Você selecionou', parcelas, 'Parcelas')



