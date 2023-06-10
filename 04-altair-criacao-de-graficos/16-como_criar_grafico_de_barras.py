import streamlit as st
import altair as alt
import pandas as pd

fonte = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

fonte # imprime o dataframe

grafico_barras=alt.Chart(fonte).mark_bar().encode(
    x='a',
    y='b',
    color='a', # nesse caso setamos para que cada rotulo tenha uma cor diferente
    tooltip=['a','b'] # essa opcao fará com que ao passar por cima apareça uma tooltip (ajuda no gráfico)
)

rotulo_barra=grafico_barras.mark_text(
    dy=-8, # posicao do rótulo em relaçao a barra
    size=17 # tamanho do texto do rótulo(acima das barras)
).encode(
    text='b' # o que vai aparecer no rótulo (acima das barras, valor de 'b')
)

st.subheader('Abaixo a representação do dataset de cima com representação de BARRAS:')

# use_container_width= True faz com que ele use toda a largura do container para esse gráfico
# o +rotulo adiciona o rótulo escolhido criado acima (numeros acima das barras para facilitar saber o valor de cada barra ao visualizar o grafico)
st.altair_chart(grafico_barras+rotulo_barra, use_container_width=True)




# VAMOS CRIAR UM NOVO GRAFICO DE BARRAS COM O MESMO DATAFRAME

grafico_barras_novo=alt.Chart(fonte).mark_bar(
    # usamos esses argumentos abaixo para arredondar a parte de cima do grafico de barras
    cornerRadiusTopLeft=10,
    cornerRadiusTopRight=10
).encode(
    x=alt.X('a',sort='y'), # estamos classificando no menor para o maior em relacao ao eixo y nesse caso
    # x=alt.X('a',sort='-y') # nesse caso ficaria classificado do maior para o menor (-y)
    y='b',

    # abaixo colocamos uma condicao para que caso o valor de y('b') seja maior que 43 a cor da barra seja azul, caso contrario a cor da barra será preta
    color=alt.condition(
        alt.datum.b>43,
        alt.value('steelblue'),
        alt.value('gray')
    )
)


rotulo=grafico_barras_novo.mark_text(
    align='center',
    baseline='middle',
    size=14,
    dy=-10
).encode(text='b')


# aqui criamos uma linha media na cor vermelha para mostrar no grafico onde está a média em relacao aos valores de y('b')
linha_media=alt.Chart(fonte).mark_rule(color='red').encode(
    y='mean(b)'
)

st.subheader('NOVO GRAFICO DE BARRAS')

st.altair_chart(grafico_barras_novo+rotulo+linha_media,use_container_width=True)