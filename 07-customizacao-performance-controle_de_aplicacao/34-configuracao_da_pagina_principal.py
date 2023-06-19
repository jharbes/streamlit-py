from turtle import color
import pandas as pd
import streamlit as st
import altair as alt


# SET PAGE CONFIG - permite algumas configuracoes como titulo da aplicacao, icones, layout, configurar sidebar se inicia expandido ou colapsado, configurar links nos elementos na parte superior direita da tela
# SET PAGE CONFIG - precisa ser o primeiro elemento do codigo
st.set_page_config(
    # muda o titulo da pagina (na parte superior do browser)
    page_title='Os Homens mais ricos do mundo',

    # page icon adiciona um favicon para a pagina
    page_icon='📈',

    # layout pode ser centered ou wide
    layout='centered',

    # se o sidebar começa collapsed, expanded ou auto
    initial_sidebar_state='expanded',

    # altera configuracoes do menu superior a direita do streamlit
    menu_items={
        'Get Help': 'https://www.meusite.com.br',
        'Report a bug':'http://www.meuoutrosite.com.br',
        'About': 'Esse app foi desenvolvido por J.Harbes',
    }
)




df = pd.read_excel(
    io = '../Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name='ricos',
    usecols='A:B',
    nrows=10
)


# Cria um sidebar para filtrar os bilionarios no df e gráfico
st.sidebar.header('Filtre aqui:')
bilionarios=st.sidebar.multiselect(
    'Selecione os bilionários:',
    options=df['Nome'].unique(),
    default=df['Nome'].unique()
)

# Cria uma nova versão do df conforme filtros aplicados
df_filtrado=df.query(
    'Nome == @bilionarios'
)



graf_pizza = alt.Chart(df_filtrado).mark_arc(
    innerRadius=0,
    outerRadius=150
).encode(
    theta = alt.Theta(field='Fortuna', type='quantitative', stack=True),
    color=alt.Color(
        field='Nome', 
        type='nominal',
        #legend=None
    ),
    tooltip = ['Nome', 'Fortuna']
).properties(width=700, height=450)

rotuloNome = graf_pizza.mark_text(radius=200, size=14).encode(text='Nome')
rotuloValor = graf_pizza.mark_text(radius=165, size=14).encode(text='Fortuna')


st.header('Gráfico de Pizza/Arco')
st.subheader('Os mais ricos do mundo')
st.altair_chart(graf_pizza+rotuloNome+rotuloValor)