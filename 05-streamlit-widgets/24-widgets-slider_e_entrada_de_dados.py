import pandas as pd
import streamlit as st
from datetime import *


### SLIDER
st.subheader('Slider de valor pontual')

# a variavel parcelas recebera o valor do slider
# os valores 0 e 60 conforme estão configurados são os limitantes do slider (minimo e maximo) e 30 será o valor inicial que aparecerá quando carregar inicialmente
parcelas = st.slider(
    'Com quantas parcelas deseja simular?', 0, 60, 30
)

st.write('Você selecionou', parcelas, 'Parcelas')




st.subheader('Slider de intervalo')
# nesse caso nós iremos escolher um intervalo e nao um valor pontual
# os dois primeiros parametros numericos serão os limitantes do slider e a tupla seguinte a esses argumentos será o intervalo inicial ao carregar a pagina
intervalo=st.slider(
    'Qual o intervalo desejado?',
    0.0, 100.0, (25.0, 75.0)
)

st.write('Intervalo: ',intervalo)




### DATAS
st.subheader('Datas')


# primeiro parâmetro será o texto informativo, segundo parâmetro será a data inicial (onde poderemos mudar e escolher a data desejada)
data=st.date_input(
    'Selecione a data desejada:',
    datetime.now()
)

st.write('A data selecionado foi: ',data)