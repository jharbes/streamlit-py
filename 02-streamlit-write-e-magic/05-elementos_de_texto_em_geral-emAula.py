import streamlit as st

# Vamos agora enumerar os tipos de texto em geral do streamlit

st.title('Este é o título')
st.header('Header do streamlit')
st.subheader('Subheader do streamlit')

# os dois asteristicos (**) em volta da palavra média coloca ela em negrito
# um asteristico em volta coloca a palavra em itálico
# em anexo temos uma figura que mostra todos os tipos de marcacao para o markdown
st.markdown('A nota dos alunos foi em **média** maior que no *semestre* pasado, o markdown possui varios tipos de marcações que estao enumerados em uma imagem em anexo')

st.caption('Este é um caption, ele gera um contraste reduzido para textos de importância secundária')


# podemos também escrever exemplos de código no streamlit conforme abaixo, observe a diferenca dos tipos de aspas para que nao haja erro de interpretação pela linguagem:
code='''if (fome>0):
    return "ir para geladeira"
else:
    return "estudar Streamlit"'''
st.code(code,language='python')


# st.text produz textos 'sem formatação'
st.text('Este é um texto usando st.text(), ele é gerado "sem formatação"')


# Latex https://katex.org/docs/supported.html
# o streamlit dá suporte para latex, muito utilizado para fórmulas matemáticas mais detalhes utilizar a página acima
st.latex('\int x²+y²+32ab \isin x²+y²+z²')