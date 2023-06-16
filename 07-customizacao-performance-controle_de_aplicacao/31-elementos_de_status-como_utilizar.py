import streamlit as st
import time


# inserindo uma barra de progresso no aplicativo
myBar=st.progress(0)
for num in range(100):
    time.sleep(0.01)
    myBar.progress(num+1)



# inserindo um spinner no aplicativo
with st.spinner('Aguarde...'):
    time.sleep(1)
st.success('Seu dataset foi carregado com sucesso!') # mensagem de sucesso (padrao verde)


# mensagem de erro (padrao vermelho)
st.error('Caracter inválido')


# mensagem de aviso, alerta (padrao amarelo)
st.warning('Data fora do intervalo padrão')


# mensagem informativa (padrao azul)
st.info('Os resultados já foram carregados na base.')


# mensagem de erro do tipo RuntimeError (acontece quando o programa é acionado para fazer algp para que nao foi programado)
e=RuntimeError('Exceção do tipo RuntimeError')
st.exception(e)



# animações do streamlit

# caindo neve
st.snow()

# balôes subindo
st.balloons()