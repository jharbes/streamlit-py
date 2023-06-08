import streamlit as st
import pandas as pd
import numpy as np


st.subheader('Exemplo 6 - Temperatura')

col1, col2, col3 = st.columns(3)

col1.metric("Temperatura","25 ºC","2 ºC")

col2.metric("Vento","10 Km/h","-8%")

col3.metric("Humidade","86%","4%",delta_color='inverse') # nesse caso o delta color 'inverse' inverte a cor do positivo de verde para vermelho, se o delta_color for 'off' ele deixa a cor da variação em cinza

