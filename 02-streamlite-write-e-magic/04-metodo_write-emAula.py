import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Método write é similar ao MAGIC
# Porém ele faz uma série de verificações e dependendo do argumento da funcao ele vai imprimir de uma maneira diferente

st.write('Este é um texto')


#Exemplo 2
st.write(pd.DataFrame({
    'Coluna A': [1, 2,3,4,5],
    'Coluna B': ["Cachorro", "Gato", "Cavalo","Vaca","Zebra"],
}))


#Exemplo 3
array = [1, 2, "abc", "Martin", True]
st.write(array)

#Exemplo 4
st.write('aqui teremos uma array:', array)



df=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

c=alt.Chart(df).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
)

st.write(df)
st.write(c)