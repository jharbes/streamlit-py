import streamlit as st

st.header('Expander')

st.line_chart({'data':[1,5,2,6,2,1]})


# o expander funciona como uma caixa retrátil (pode estar aberta ou fechada) usada em geral para colocar informações acerca de algum assunto, normalmente sobre os graficos ou datasets presentes na pagina
with st.expander('Ver detalhes'):
    st.write("""
    Este é um exemplo de Expander,
    Você vai ver como usá-lo.
    """)
    st.image('../Mídia/dice.jpg')