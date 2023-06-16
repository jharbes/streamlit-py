import streamlit as st

st.header('Expander')
st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("Ver detalhes"):
     st.write("""
         Esse é um exemplo de jogadas aleatórias de Dados.
         Você pode colocar suas análises gráficas dentro
         de um expander como este.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg",width=600)