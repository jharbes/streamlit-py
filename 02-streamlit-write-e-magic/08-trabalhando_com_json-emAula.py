import streamlit as st

meuObjeto={
    'banana':'amarela',
    'limão':'verde',
    'laranja':'laranja'
}

# sera impresso a variavel no formato json, com pares de chave valor
st.json(meuObjeto)