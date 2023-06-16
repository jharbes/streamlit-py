import streamlit as st
import numpy as np

col1,col2,col3,col4=st.columns(4)


with col1:
    st.subheader('Coluna 1')
    st.image('../Mídia/cat.jpg')

with col2:
    st.subheader('Coluna 2')
    st.image('../Mídia/dog.jpg')

with col3:
    st.subheader('Coluna 3')
    st.image('../Mídia/owl.jpg')

with col4:
    st.subheader('Coluna 4')
    st.image('../Mídia/dog_2.jpg')


# estamos definindo aqui que queremos duas colunas, sendo que a primeira terá o triplo do tamanho da segunda, razao 3:1 entre as colunas
# gap='large' (small,medium or large) distancia entre as colunas

col_1,col_2=st.columns([3,1],gap='large')


# gerando um dataset de numeros aleatorios com 100 numeros em uma coluna
data=np.random.randn(100,1)


# colocaremos o grafico de linha do dataset na primeira coluna
col_1.line_chart(data)

# na segunda coluna escreveremos os dados referente ao dataset
col_2.write(data)