import streamlit as st
import pandas as pd
import numpy as np

st.header('Aula de Dataframe')


df=pd.DataFrame(
    np.random.randn(5,5),
    columns=('col %d' %i for i in range(5))
)

# maneiras de imprimir o dataframe, todas terao o output igual:
st.dataframe(df)
st.write(df)
df




st.subheader('Exemplo 2 - Alterando dimensões')

# nesse caso nós imprimimos igualmente o dataframe mas limitamos a janela de utilização dele a 300x200, nesse caso isso gerou barras de rolagem para sua visualizacao ja que esse tamanho nao comporta todo o dataframe
st.dataframe(df,300,200)



st.subheader('Exemplo 3 - Dando um destaque nos maiores valores')

# observe que nesse caso ele marcará o maior valor baseado em cada COLUNA, para que seja o maior valor baseado em linha usariamos axis=1
st.dataframe(df.style.highlight_max(axis=0))



st.header('TABLE - Exemplo similar ao Dataframe')

# tambem retorna o dataframe porem com forma de visualizacao diferente (espaçamento maior, menor número de casas decimais, etc)
st.table(df)